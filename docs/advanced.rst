Advanced Features
=================

mathparse supports advanced mathematical operations including constants, functions, and complex expressions.

Mathematical Constants
-----------------------

mathparse includes built-in mathematical constants that can be used in expressions:

Available Constants
+++++++++++++++++++

.. list-table:: Built-in Constants
   :widths: 15 25 60
   :header-rows: 1

   * - Constant
     - Value
     - Example Usage
   * - pi
     - 3.141693
     - ``mathparse.parse('pi * 2')``
   * - e
     - 2.718281
     - ``mathparse.parse('e * 3')``

**Examples:**

.. code-block:: python

    from mathparse import mathparse

    # Using pi
    area = mathparse.parse('pi * 5 * 5')  # Area of circle with radius 5
    # Returns: 78.54225

    # Using e (Euler's number)
    result = mathparse.parse('e ^ 2')     # e squared
    # Returns: 7.389056

    # Combining constants
    result = mathparse.parse('pi + e')
    # Returns: 5.859974

Mathematical Functions
----------------------

Unary Functions
+++++++++++++++

mathparse supports unary functions that operate on a single value:

.. list-table:: Unary Functions
   :widths: 20 30 50
   :header-rows: 1

   * - Function
     - Description
     - Example
   * - sqrt
     - Square root
     - ``mathparse.parse('sqrt 16')`` → 4.0
   * - log
     - Base-10 logarithm
     - ``mathparse.parse('log 100')`` → 2.0

**Examples:**

.. code-block:: python

    from mathparse import mathparse

    # Square root
    result = mathparse.parse('sqrt 25')
    # Returns: 5.0

    # Square root with expressions
    result = mathparse.parse('sqrt (9 + 16)')
    # Returns: 5.0

    # Logarithm
    result = mathparse.parse('log 1000')
    # Returns: 3.0

    # Combining functions with constants
    result = mathparse.parse('sqrt pi')
    # Returns: 1.7724530

Word-Based Function Usage
+++++++++++++++++++++++++

Some languages support word-based function syntax:

.. code-block:: python

    # English
    result = mathparse.parse('square root of sixteen', language='ENG')
    # Returns: 4.0

    result = mathparse.parse('four squared', language='ENG')
    # Returns: 16

    result = mathparse.parse('three cubed', language='ENG')
    # Returns: 27

    # Portuguese
    result = mathparse.parse('raiz quadrada de dezesseis', language='POR')
    # Returns: 4.0

    result = mathparse.parse('quatro ao quadrado', language='POR')
    # Returns: 16

    # Greek
    result = mathparse.parse('τετραγωνική ρίζα του δεκαέξι', language='GRE')
    # Returns: 4.0

    result = mathparse.parse('τέσσερα στο τετράγωνο', language='GRE')
    # Returns: 16

Complex Expression Parsing
---------------------------

mathparse can handle complex mathematical expressions with multiple operations, parentheses, and order of operations.

Order of Operations
+++++++++++++++++++

mathparse follows standard mathematical order of operations (PEMDAS):

1. **Parentheses** - Operations inside parentheses first
2. **Exponents** - Powers and roots
3. **Multiplication and Division** - Left to right
4. **Addition and Subtraction** - Left to right

**Examples:**

.. code-block:: python

    from mathparse import mathparse

    # Standard order of operations
    result = mathparse.parse('2 + 3 * 4')
    # Returns: 14 (not 20)

    # Using parentheses to change order
    result = mathparse.parse('(2 + 3) * 4')
    # Returns: 20

    # Complex expression
    result = mathparse.parse('2 * (3 + 4) ^ 2 - 5')
    # Returns: 93

Nested Expressions
++++++++++++++++++

.. code-block:: python

    # Multiple levels of nesting
    result = mathparse.parse('((2 + 3) * (4 + 6)) / 5')
    # Returns: 10.0

    # With functions and constants
    result = mathparse.parse('sqrt((pi * 4) ^ 2)')
    # Returns: 12.566772

    # Complex word-based expression
    result = mathparse.parse(
        '(five times six) plus (square root of sixteen)',
        language='ENG'
    )
    # Returns: 34.0

Large Number Support
++++++++++++++++++++

mathparse can parse and calculate with large numbers expressed in words:

.. code-block:: python

    # Large numbers
    result = mathparse.parse(
        'two million three hundred thousand plus fifty thousand',
        language='ENG'
    )
    # Returns: 2350000

    # Complex calculations with large numbers
    result = mathparse.parse(
        'one million divided by two thousand',
        language='ENG'
    )
    # Returns: 500.0

Mixed Operations
++++++++++++++++

.. code-block:: python

    # Constants, functions, and arithmetic
    result = mathparse.parse('(sqrt 16) * pi + e')
    # Returns: 15.284454

    # Powers with functions
    result = mathparse.parse('(sqrt 9) ^ 3')
    # Returns: 27.0

    # Logarithms with multiplication
    result = mathparse.parse('log 100 * 5')
    # Returns: 10.0

Error Handling and Edge Cases
------------------------------

Division by Zero
++++++++++++++++

mathparse handles division by zero gracefully:

.. code-block:: python

    result = mathparse.parse('10 / 0')
    # Returns: 'undefined'

    result = mathparse.parse('six divided by zero', language='ENG')
    # Returns: 'undefined'

Invalid Expressions
+++++++++++++++++++

.. code-block:: python

    from mathparse.mathparse import PostfixTokenEvaluationException

    try:
        # Invalid operator
        result = mathparse.parse('5 & 3')  # & is not a valid operator
    except PostfixTokenEvaluationException as e:
        print(f"Evaluation error: {e}")

Decimal Precision
+++++++++++++++++

mathparse uses Python's ``Decimal`` module for division to maintain precision:

.. code-block:: python

    result = mathparse.parse('1 / 3')
    # Returns: Decimal('0.3333333333333333333333333333')

    # Convert to float if needed
    float_result = float(mathparse.parse('1 / 3'))
    # Returns: 0.3333333333333333

Performance Considerations
--------------------------

Expression Complexity
+++++++++++++++++++++

- Simple expressions parse very quickly
- Complex nested expressions require more processing time
- Word-based parsing is slower than numeric parsing due to text processing

Memory Usage
++++++++++++

- mathparse has minimal memory requirements
- Large numbers are handled efficiently using Python's built-in numeric types
- No significant memory overhead for complex expressions

Best Practices
++++++++++++++

1. **Use numeric expressions when possible** for better performance
2. **Validate language codes** before processing user input
3. **Handle exceptions** appropriately in production code
4. **Consider caching** results for frequently calculated expressions

.. code-block:: python

    from mathparse import mathparse
    from mathparse.mathwords import InvalidLanguageCodeException
    from mathparse.mathparse import PostfixTokenEvaluationException

    def safe_parse(expression, language=None):
        """Safely parse a mathematical expression with error handling."""
        try:
            return mathparse.parse(expression, language=language)
        except InvalidLanguageCodeException:
            return "Error: Invalid language code"
        except PostfixTokenEvaluationException:
            return "Error: Could not evaluate expression"
        except Exception as e:
            return f"Error: {str(e)}"

    # Usage
    result = safe_parse('five plus three', 'ENG')
    # Returns: 8

    result = safe_parse('invalid expression', 'INVALID')
    # Returns: "Error: Invalid language code"
