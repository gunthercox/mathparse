API Reference
=============

Core Parsing Functions
----------------------

.. automodule:: mathparse.mathparse
   :no-index:
   :members:

The main parsing module contains all the core functionality for mathematical expression parsing.

Main Parse Function
+++++++++++++++++++

.. autofunction:: mathparse.mathparse.parse

This is the primary function for parsing mathematical expressions. It accepts both numeric and word-based expressions.

**Parameters:**

* ``string`` (str): The mathematical expression to parse
* ``language`` (str, optional): ISO 639-2 language code for word-based parsing

**Returns:**

* ``int``, ``float``, or ``str``: The result of the mathematical expression, or 'undefined' for division by zero

**Example:**

.. code-block:: python

    from mathparse import mathparse
    
    # Numeric expression
    result = mathparse.parse('2 + 3 * 4')
    # Returns: 14
    
    # Word-based expression
    result = mathparse.parse('five times six plus ten', language='ENG')
    # Returns: 40

Expression Extraction
+++++++++++++++++++++

.. autofunction:: mathparse.mathparse.extract_expression

This function extracts mathematical expressions from sentences containing additional text.

**Example:**

.. code-block:: python

    # Extract from a question
    expression = mathparse.extract_expression("What is 5 plus 3?", language='ENG')
    # Returns: "5 plus 3"
    
    result = mathparse.parse(expression, language='ENG')
    # Returns: 8

Tokenization Functions
++++++++++++++++++++++

.. autofunction:: mathparse.mathparse.tokenize

Converts a string into mathematical tokens that can be processed.

.. autofunction:: mathparse.mathparse.replace_word_tokens

Replaces word-based mathematical terms with their symbolic equivalents.

Evaluation Functions
++++++++++++++++++++

.. autofunction:: mathparse.mathparse.to_postfix

Converts mathematical tokens to postfix notation for evaluation.

.. autofunction:: mathparse.mathparse.evaluate_postfix

Evaluates a postfix expression and returns the result.

Utility Functions
+++++++++++++++++

.. autofunction:: mathparse.mathparse.is_int
.. autofunction:: mathparse.mathparse.is_float
.. autofunction:: mathparse.mathparse.is_constant
.. autofunction:: mathparse.mathparse.is_unary
.. autofunction:: mathparse.mathparse.is_binary
.. autofunction:: mathparse.mathparse.is_symbol
.. autofunction:: mathparse.mathparse.is_word

Language and Word Support
--------------------------

.. automodule:: mathparse.mathwords
   :no-index:
   :members:

This module provides language-specific mathematical terms and utility functions.

Language Functions
++++++++++++++++++

.. autofunction:: mathparse.mathwords.words_for_language

Returns all mathematical words for a specific language.

**Parameters:**

* ``language_code`` (str): ISO 639-2 language code

**Returns:**

* ``list``: All mathematical words for the language

**Example:**

.. code-block:: python

    from mathparse.mathwords import words_for_language
    
    english_words = words_for_language('ENG')
    # Returns: ['plus', 'minus', 'times', 'one', 'two', ...]

.. autofunction:: mathparse.mathwords.word_groups_for_language

Returns organized groups of mathematical words (operators, numbers, scales) for a language.

**Parameters:**

* ``language_code`` (str): ISO 639-2 language code

**Returns:**

* ``dict``: Dictionary containing word groups

**Example:**

.. code-block:: python

    from mathparse.mathwords import word_groups_for_language
    
    groups = word_groups_for_language('ENG')
    # Returns: {
    #     'binary_operators': {'plus': '+', 'minus': '-', ...},
    #     'numbers': {'one': 1, 'two': 2, ...},
    #     'scales': {'hundred': 100, 'thousand': 1000, ...}
    # }

Constants and Functions in Utils
++++++++++++++++++++++++++++++++

Mathematical Constants in Utils
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

mathparse includes common mathematical constants:

.. py:data:: mathparse.mathwords.CONSTANTS

   Dictionary of mathematical constants available in expressions.
   
   Available constants:
   
   * ``pi``: 3.141693
   * ``e``: 2.718281

**Example:**

.. code-block:: python

    result = mathparse.parse('pi * 2')
    # Returns: 6.283386

Unary Functions in Utils
~~~~~~~~~~~~~~~~~~~~~~~~

.. py:data:: mathparse.mathwords.UNARY_FUNCTIONS

   Dictionary of available unary mathematical functions.
   
   Available functions:
   
   * ``sqrt``: Square root function
   * ``log``: Base-10 logarithm function

**Example:**

.. code-block:: python

    result = mathparse.parse('sqrt 16')
    # Returns: 4.0
    
    result = mathparse.parse('log 100')
    # Returns: 2.0

Binary Operators
~~~~~~~~~~~~~~~~

.. py:data:: mathparse.mathwords.BINARY_OPERATORS

   Set of supported binary mathematical operators.
   
   Includes: ``{'^', '*', '/', '+', '-'}``

Exceptions
----------

.. autoexception:: mathparse.mathparse.PostfixTokenEvaluationException

   Raised when there's an error evaluating postfix tokens.

.. autoexception:: mathparse.mathwords.InvalidLanguageCodeException

   Raised when an invalid or unsupported language code is provided.

**Example:**

.. code-block:: python

    from mathparse import mathparse
    from mathparse.mathwords import InvalidLanguageCodeException
    
    try:
        result = mathparse.parse('five plus three', language='INVALID')
    except InvalidLanguageCodeException as e:
        print(f"Language error: {e}")

Language Codes
--------------

.. py:data:: mathparse.mathwords.LANGUAGE_CODES

   List of supported ISO 639-2 language codes.
   
   Currently supported: ``['ENG', 'FRE', 'GER', 'GRE', 'ITA', 'MAR', 'RUS', 'POR']``
