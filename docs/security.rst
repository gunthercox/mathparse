Security
========

Why use mathparse instead of ``eval()``?
-----------------------------------------

A requirement in certain Python applications is evaluating mathematical expressions provided by users (e.g., in chat bots, calculators, or form inputs).

The built-in Python function ``eval()`` is often the first tool developers reach for, but it introduces **critical security vulnerabilities**. mathparse was designed specifically to solve this problem by providing a safe, limited-scope parser that handles natural language.

The Danger of ``eval()``
-------------------------

Using ``eval()`` on untrusted input allows a user to execute **arbitrary code** on your server. If a malicious user inputs a system command instead of a math equation, your application will execute it.

**The "Bad" Example:**

.. code-block:: python

   # DANGEROUS: Do not use with user input
   user_input = "__import__('os').system('rm -rf /')"

   # This executes the system command!
   result = eval(user_input)

The mathparse Solution
-----------------------

mathparse scans the string for known mathematical patterns, numbers, and operators.
If the input contains system commands or malicious Python code, mathparse is not capable of executing it.
Unrecognized tokens will cause mathparse to raise a ``PostfixTokenEvaluationException``, preventing any code execution and ensuring the safety of your application.

**The Safe Example:**

.. code-block:: python

   from mathparse import mathparse
   from mathparse.mathparse import PostfixTokenEvaluationException

   # SAFE: mathparse rejects invalid input
   user_input = "__import__('os').system('rm -rf /')"

   try:
       result = mathparse.parse(user_input)
   except PostfixTokenEvaluationException as e:
       print(f"Invalid input: {e}")
       # Output: Unsupported mathematical term: "__import__"

Feature Comparison
------------------

.. list-table::
   :widths: 30 35 35
   :header-rows: 1

   * - Feature
     - mathparse
     - Python eval()
   * - **Security**
     - ✅ **Safe** (Token validation)
     - ❌ **Unsafe** (Executes arbitrary code)
   * - **Natural Language**
     - ✅ **Yes** (e.g., "five plus 2")
     - ❌ **No** (SyntaxError)
   * - **Word-to-Number**
     - ✅ **Yes** ("two hundred" → 200)
     - ❌ **No**
   * - **Scope**
     - Mathematical expressions only
     - Full Python environment access

Natural Language Support
------------------------

Beyond security, ``eval()`` fails when users type naturally. mathparse bridges the gap between spoken language and mathematical evaluation.

.. code-block:: python

   # eval() crashes here:
   # SyntaxError: invalid syntax
   eval("five plus seven")

   # mathparse handles it natively:
   mathparse.parse("five plus seven", language='ENG')
   # >> 12

How mathparse Ensures Security
-------------------------------

mathparse achieves security through a five-phase parsing and evaluation pipeline:

1. **Word Replacement**
   If a language is specified, natural language words (e.g., "five", "plus") are replaced with their symbolic equivalents (e.g., ``5``, ``+``) using language-specific dictionaries. Compound numbers like "twenty one" are converted to ``(20 + 1)``.

2. **Tokenization**
   The resulting string is broken into individual tokens (numbers, operators, parentheses).

3. **Unary Operator Preprocessing**
   Minus signs that represent negation (e.g., the leading ``-`` in ``-3 + 5``) are converted to the ``neg`` unary function to distinguish them from binary subtraction.

4. **Postfix Conversion with Token Validation (RPN)**
   Tokens are converted to Reverse Polish Notation (postfix), which eliminates operator precedence ambiguity. During this conversion, each token is checked against an allow-list of known mathematical symbols. Unknown tokens (like ``__import__``, ``os.system``, or ``eval``) are immediately rejected with a ``PostfixTokenEvaluationException``.

5. **Stack-Based Evaluation**
   The postfix expression is evaluated using a controlled stack-based algorithm with predefined operations. **No Python eval() is used anywhere in the codebase.**

This architecture ensures that only allow-listed mathematical operations can be performed, malicious code never reaches the execution phase.

What's Allowed
--------------

mathparse accepts these mathematical elements:

**Binary Operators:**

* Arithmetic: ``+``, ``-``, ``*``, ``/``
* Exponentiation: ``^``
* Decimal point: ``.`` (e.g., "three point five" → 3.5)

**Unary Functions:**

* ``sqrt`` - Square root
* ``log`` - Base-10 logarithm
* ``neg`` - Negation

**Mathematical Constants:**

* ``pi`` (also ``π``) - Approximately 3.141593
* ``e`` - Approximately 2.718281

**Grouping:**

* Parentheses: ``(`` and ``)``

**Natural Language:**

* Number words (language-dependent): "five", "twenty", "hundred", etc.
* Operator words (language-dependent): "plus", "times", "minus", etc.
* Function phrases (language-dependent): "square root of", "squared", etc.

What Gets Blocked
-----------------

Inputs such as the following cannot be evaluated by mathparse:

* **Import statements:** ``import``, ``__import__``, ``from ... import``
* **Function calls:** Except allow-listed functions (``sqrt``, ``log``)
* **Object attribute access:** ``object.attribute``, ``os.system``
* **File operations:** ``open()``, ``read()``, ``write()``
* **Network operations:** ``socket``, ``urllib``, ``requests``
* **Variable assignment:** ``x = 5``
* **Control flow:** ``if``, ``while``, ``for``
* **Built-in functions:** ``print()``, ``exec()``, ``compile()``

Best Practices for Production
------------------------------

To use mathparse securely with user input in production environments:

Exponentiation rejects exponents with an absolute value above 10,000 and
results estimated to have more than 4,000 digits, raising
``PostfixTokenEvaluationException``. These limits do not bound all parsing or
arithmetic costs. Applications processing untrusted input should also limit
input size and enforce time and memory limits externally.

**1. Always Use Error Handling**

.. code-block:: python

   from mathparse import mathparse
   from mathparse.mathparse import PostfixTokenEvaluationException

   def safe_calculate(user_input: str, language: str = 'ENG') -> str:
       """
       Safely evaluate a mathematical expression from user input.

       Returns the result as a string, or an error message.
       """
       try:
           result = mathparse.parse(user_input, language=language)
           return str(result)
       except PostfixTokenEvaluationException as e:
           return f"Invalid expression: {e}"
       except Exception as e:
           return f"Error: {e}"

   # Usage
   print(safe_calculate("2 + 2"))              # "4"
   print(safe_calculate("import os"))          # "Invalid expression: ..."
   print(safe_calculate("5 / 0"))              # "undefined"

**2. Handle Division by Zero**

mathparse returns the string ``'undefined'`` for division by zero instead of raising an exception:

.. code-block:: python

   result = mathparse.parse("5 / 0")

   if result == 'undefined':
       print("Cannot divide by zero")
   else:
       print(f"Result: {result}")

**3. Validate Input Length**

For production systems, consider limiting expression length and complexity to prevent resource exhaustion:

.. code-block:: python

   MAX_EXPRESSION_LENGTH = 1000
   MAX_NESTING_DEPTH = 50

   def validate_input(expression: str) -> bool:
       if len(expression) > MAX_EXPRESSION_LENGTH:
           raise ValueError("Expression too long")

       # Check nesting depth
       depth = 0
       max_depth = 0
       for char in expression:
           if char == '(':
               depth += 1
               max_depth = max(max_depth, depth)
           elif char == ')':
               depth -= 1

       if max_depth > MAX_NESTING_DEPTH:
           raise ValueError("Expression too deeply nested")

       return True

**4. Sanitize stopwords**

When using natural language input, provide appropriate stopwords to filter out non-mathematical terms:

.. code-block:: python

   common_stopwords = {
       'the', 'a', 'an', 'is', 'what', 'equals', 'calculate', 'compute'
   }

   result = mathparse.parse(
       "what is five plus three",
       language='ENG',
       stopwords=common_stopwords
   )
   # Returns: 8

Additional Security Considerations
-----------------------------------

**Rate Limiting**

In web applications, implement rate limiting to prevent abuse:

.. code-block:: python

   from functools import lru_cache
   import time

   @lru_cache(maxsize=1000)
   def rate_limited_parse(expression: str, timestamp: int):
       """Cache results and implicitly rate-limit by time windows."""
       return mathparse.parse(expression)

   # Usage
   result = rate_limited_parse("2 + 2", int(time.time() // 60))

**Logging Suspicious Patterns**

Log expressions that raise exceptions for security monitoring:

.. code-block:: python

   import logging

   logger = logging.getLogger(__name__)

   def monitored_parse(expression: str, user_id: str):
       try:
           return mathparse.parse(expression)
       except PostfixTokenEvaluationException as e:
           logger.warning(
               f"Suspicious input from user {user_id}: {expression}"
           )
           raise

See Also
--------

* :doc:`postfix` - Technical details on postfix evaluation and security architecture
* :doc:`quickstart` - Getting started with mathparse and basic usage patterns
* :doc:`examples` - Real-world usage examples with proper error handling
* :doc:`languages` - Multi-language support and natural language processing
