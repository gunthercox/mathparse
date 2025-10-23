Quick Start Guide
=================

Get started with mathparse in 30 seconds! This guide covers the essentials to get you up and running quickly.

Installing mathparse
--------------------

Install mathparse using pip:

.. code-block:: bash

    pip install mathparse

Mathparse should now be installed and ready to use.
mathparse with Python 3.9 - 3.13 and has **zero dependencies**.

Your First Calculation
-----------------------

.. code-block:: python

    from mathparse import mathparse

    # Basic calculation
    result = mathparse.parse('2 + 3 * 4')
    print(result)  # 14

5-Minute Tutorial
-----------------

1. Basic Arithmetic
+++++++++++++++++++

.. code-block:: python

    from mathparse import mathparse

    # Simple operations
    mathparse.parse('10 + 5')        # 15
    mathparse.parse('20 - 8')        # 12
    mathparse.parse('6 * 7')         # 42
    mathparse.parse('100 / 4')       # 25.0
    mathparse.parse('2 ^ 8')         # 256 (exponentiation)

2. Natural Language (English)
++++++++++++++++++++++++++++++

.. code-block:: python

    # Parse math in plain English
    mathparse.parse('five plus three', language='ENG')
    # Returns: 8

    mathparse.parse('twenty times four', language='ENG')
    # Returns: 80

    mathparse.parse('one hundred divided by five', language='ENG')
    # Returns: 20.0

3. Other Languages
++++++++++++++++++

.. code-block:: python

    # French
    mathparse.parse('cinq plus trois', language='FRE')
    # Returns: 8

    # Spanish
    mathparse.parse('diez más cinco', language='ESP')
    # Returns: 15

    # German
    mathparse.parse('zwanzig mal drei', language='GER')
    # Returns: 60

    # Simplified Chinese
    mathparse.parse('五 加 三', language='CHI')
    # Returns: 8

**Supported languages:** English (ENG), French (FRE), Spanish (ESP), German (GER), 
Italian (ITA), Portuguese (POR), Russian (RUS), Greek (GRE), Ukrainian (UKR), 
Dutch (DUT), Thai (THA), Marathi (MAR), Simplified Chinese (CHI)

4. Complex Expressions
+++++++++++++++++++++++

.. code-block:: python

    # Order of operations (PEMDAS)
    mathparse.parse('2 + 3 * 4')
    # Returns: 14 (multiplication first)

    # Parentheses for grouping
    mathparse.parse('(2 + 3) * 4')
    # Returns: 20

    # Nested expressions
    mathparse.parse('((5 + 3) * 2) - 4')
    # Returns: 12

5. Mathematical Functions
++++++++++++++++++++++++++

.. code-block:: python

    # Square root
    mathparse.parse('sqrt 16')
    # Returns: 4.0

    # Logarithm (base 10)
    mathparse.parse('log 100')
    # Returns: 2.0

    # Constants
    mathparse.parse('pi * 2')
    # Returns: 6.283386

    mathparse.parse('e ^ 2')
    # Returns: 7.389056

6. Decimal Numbers (Natural Language)
+++++++++++++++++++++++++++++++++++++++

.. code-block:: python

    # English decimal notation
    mathparse.parse('five point two', language='ENG')
    # Returns: 5.2

    mathparse.parse('ten point twenty five', language='ENG')
    # Returns: 10.25

    # French uses "virgule" (comma)
    mathparse.parse('cinq virgule deux', language='FRE')
    # Returns: 5.2

Common Use Cases
----------------

Calculator Function
+++++++++++++++++++

.. code-block:: python

    from mathparse import mathparse
    from mathparse.mathparse import PostfixTokenEvaluationException

    def calculator(expression, language=None):
        """
        Safe calculator function.
        """
        try:
            result = mathparse.parse(expression, language=language)
            if result == 'undefined':
                return "Error: Division by zero"
            return result
        except PostfixTokenEvaluationException:
            return "Error: Invalid expression"

    # Usage
    print(calculator('2 + 3'))
    # Output: 5

    print(calculator('five times six', language='ENG'))
    # Output: 30

Natural Language Question Answering
++++++++++++++++++++++++++++++++++++

.. code-block:: python

    def answer_math_question(question, language='ENG'):
        """
        Extract and solve math from natural language.
        """
        # Extract the mathematical part
        expression = mathparse.extract_expression(question, language)

        # Calculate the result
        result = mathparse.parse(expression, language=language)

        return f"The answer is {result}"

    # Usage
    answer_math_question("What is five plus seven?")
    # Output: "The answer is 12"

Multi-Language Support
++++++++++++++++++++++

.. code-block:: python

    def multilingual_calculator(expression, language):
        """
        Calculator supporting multiple languages.
        """
        languages = {
            'en': 'ENG',
            'fr': 'FRE', 
            'es': 'ESP',
            'de': 'GER',
            'zh': 'CHI'
        }

        lang_code = languages.get(language)
        if not lang_code:
            return "Language not supported"

        return mathparse.parse(expression, language=lang_code)

    # Usage
    print(multilingual_calculator('cinco más tres', 'es'))
    # Output: 8

Security: Safe Alternative to eval()
-------------------------------------

**Never use eval() with user input!** It's dangerous:

.. code-block:: python

    # DANGEROUS - DON'T DO THIS!
    user_input = "__import__('os').system('rm -rf /')"
    eval(user_input)  # Could delete your entire system!

**mathparse is the safe alternative:**

.. code-block:: python

    # SAFE - Only evaluates mathematical expressions
    user_input = "__import__('os').system('ls')"
    mathparse.parse(user_input)
    # Raises PostfixTokenEvaluationException - NOT executed!

mathparse only recognizes mathematical operations, making it safe for user input:

.. code-block:: python

    # These work (mathematical operations)
    mathparse.parse('2 + 3')           # ✅ Returns 5
    mathparse.parse('sqrt 16')         # ✅ Returns 4.0
    mathparse.parse('pi * 2')          # ✅ Returns 6.283386

    # These are rejected (not mathematical)
    mathparse.parse('import os')       # ❌ Raises exception
    mathparse.parse('open("file")')    # ❌ Raises exception
    mathparse.parse('print("hello")')  # ❌ Raises exception

Handling Errors
---------------

Always handle potential errors when parsing user input:

.. code-block:: python

    from mathparse import mathparse
    from mathparse.mathwords import InvalidLanguageCodeException
    from mathparse.mathparse import PostfixTokenEvaluationException

    def safe_parse(expression, language=None):
        """
        Safely parse with comprehensive error handling.
        """
        try:
            result = mathparse.parse(expression, language=language)

            # Check for division by zero
            if result == 'undefined':
                return {'success': False, 'error': 'Division by zero'}

            return {'success': True, 'result': result}

        except InvalidLanguageCodeException:
            return {'success': False, 'error': 'Invalid language code'}
        except PostfixTokenEvaluationException as e:
            return {'success': False, 'error': f'Invalid expression: {e}'}
        except Exception as e:
            return {'success': False, 'error': f'Unexpected error: {e}'}

    # Usage
    print(safe_parse('2 + 3'))
    # Output: {'success': True, 'result': 5}

    print(safe_parse('10 / 0'))
    # Output: {'success': False, 'error': 'Division by zero'}

Next Steps
----------

Now that you know the basics, explore more:

* :doc:`examples` - Comprehensive examples and use cases
* :doc:`languages` - Complete language support documentation
* :doc:`advanced` - Mathematical functions and constants
* :doc:`postfix` - Understanding the security architecture
* :doc:`utils` - Complete API reference

Performance Tips
----------------

1. **Use numeric expressions when possible** - They're faster than natural language
2. **Cache language validation** - If processing many expressions in the same language
3. **Pre-validate user input** - Check for reasonable length/complexity before parsing

.. code-block:: python

    # Fast (numeric)
    mathparse.parse('2 + 3')

    # Slower (natural language - requires text processing)
    mathparse.parse('two plus three', language='ENG')

Getting Help
------------

* **Documentation**: https://mathparse.chatterbot.us
* **GitHub Issues**: https://github.com/gunthercox/mathparse/issues
* **PyPI**: https://pypi.org/project/mathparse/

Ready to dive deeper? Check out the :doc:`examples` page for advanced usage patterns!
