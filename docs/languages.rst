Language Support
================

mathparse supports mathematical expression parsing in multiple languages. Each language uses natural words for numbers, operators, and mathematical functions.

Supported Languages
-------------------

The following languages are supported with their ISO 639-2 language codes:

.. list-table:: Supported Languages
   :widths: 15 20 65
   :header-rows: 1

   * - Code
     - Language
     - Example
   * - CHI
     - Simplified Chinese
     - ``'五十 乘 二十 加 十'``
   * - DUT
     - Dutch
     - ``'vijftig maal twintig plus tien'``
   * - ENG
     - English
     - ``'fifty times twenty plus ten'``
   * - ESP
     - Spanish
     - ``'cincuenta por veinte más diez'``
   * - FRE
     - French
     - ``'cinquante fois vingt plus dix'``
   * - GER
     - German
     - ``'fünfzig mal zwanzig plus zehn'``
   * - GRE
     - Greek
     - ``'πενήντα επί είκοσι συν δέκα'``
   * - ITA
     - Italian
     - ``'cinquanta per venti più dieci'``
   * - MAR
     - Marathi
     - ``'पन्नास गुणाकार वीस बेरीज दहा'``
   * - POR
     - Portuguese
     - ``'cinquenta vezes vinte mais dez'``
   * - RUS
     - Russian
     - ``'пятьдесят умножить на двадцать плюс десять'``
   * - THA
     - Thai
     - ``'ห้าสิบ คูณ ยี่สิบ บวก สิบ'``
   * - UKR
     - Ukrainian
     - ``'п'ятдесят помножити на двадцять додати десять'``

Language Usage Examples
-----------------------

English (ENG)
+++++++++++++

.. code-block:: python

    from mathparse import mathparse

    # Basic arithmetic
    mathparse.parse('five plus three', language='ENG')
    >>> 8

    # Large numbers
    mathparse.parse('two thousand three hundred forty five', language='ENG')
    >>> 2345

    # Complex expressions
    mathparse.parse('seven times nine minus four', language='ENG')
    >>> 59

    # Powers and roots
    mathparse.parse('four squared', language='ENG')
    >>> 16

    mathparse.parse('square root of sixteen', language='ENG')
    >>> 4.0

French (FRE)
++++++++++++

.. code-block:: python

    # Basic arithmetic
    mathparse.parse('cinq plus trois', language='FRE')
    >>> 8

    # Multiplication
    mathparse.parse('sept fois neuf', language='FRE')
    >>> 63

    # Division
    mathparse.parse('vingt divisé par quatre', language='FRE')
    >>> 5.0

German (GER)
++++++++++++

.. code-block:: python

    # Basic arithmetic
    mathparse.parse('fünf plus drei', language='GER')
    >>> 8

    # Large numbers
    mathparse.parse('zwei tausend dreihundert', language='GER')
    >>> 2300

    # Powers
    mathparse.parse('vier hoch zwei', language='GER')
    >>> 16

Greek (GRE)
+++++++++++

.. code-block:: python

    # Basic arithmetic
    mathparse.parse('πέντε συν τρία', language='GRE')
    >>> 8

    # Multiplication
    mathparse.parse('εφτά επί εννιά', language='GRE')
    >>> 63

    # Powers and roots
    mathparse.parse('τέσσερα στο τετράγωνο', language='GRE')
    >>> 16

Italian (ITA)
+++++++++++++

.. code-block:: python

    # Basic arithmetic
    mathparse.parse('cinque più tre', language='ITA')
    >>> 8

    # Division
    mathparse.parse('venti diviso quattro', language='ITA')
    >>> 5.0

    # Powers
    mathparse.parse('quattro al quadrato', language='ITA')
    >>> 16

Portuguese (POR)
++++++++++++++++

.. code-block:: python

    # Basic arithmetic
    mathparse.parse('cinco mais três', language='POR')
    >>> 8

    # Large numbers
    mathparse.parse('mil duzentos trinta quatro', language='POR')
    >>> 1234

    # Powers and roots
    mathparse.parse('quatro ao quadrado', language='POR')
    >>> 16

    mathparse.parse('raiz quadrada de dezesseis', language='POR')
    >>> 4.0

Russian (RUS)
+++++++++++++

.. code-block:: python

    # Basic arithmetic
    mathparse.parse('пять плюс три', language='RUS')
    >>> 8

    # Multiplication
    mathparse.parse('семь умножить на девять', language='RUS')
    >>> 63

    # Powers
    mathparse.parse('четыре в квадрате', language='RUS')
    >>> 16

Marathi (MAR)
+++++++++++++

.. code-block:: python

    # Basic arithmetic - using Devanagari numerals
    mathparse.parse('पाच बेरीज तीन', language='MAR')
    >>> 8

    # Note: Marathi uses Devanagari numerals
    mathparse.parse('सात गुणाकार नऊ', language='MAR')
    >>> 63

Dutch (DUT)
+++++++++++

.. code-block:: python

    # Basic arithmetic
    mathparse.parse('vijf plus drie', language='DUT')
    >>> 8

    # Multiplication
    mathparse.parse('zes maal negen', language='DUT')
    >>> 54

    # Powers and roots
    mathparse.parse('vier kwadraat', language='DUT')
    >>> 16

    mathparse.parse('vierkantswortel van zestien', language='DUT')
    >>> 4.0

Spanish (ESP)
+++++++++++++

.. code-block:: python

    # Basic arithmetic
    mathparse.parse('cinco más tres', language='ESP')
    >>> 8

    # Multiplication
    mathparse.parse('seis por nueve', language='ESP')
    >>> 54

    # Powers and roots
    mathparse.parse('cuatro al cuadrado', language='ESP')
    >>> 16

    mathparse.parse('raiz cuadrada de dieciséis', language='ESP')
    >>> 4.0

Ukrainian (UKR)
+++++++++++++++

.. code-block:: python

    # Basic arithmetic
    mathparse.parse('п'ять додати три', language='UKR')
    >>> 8

    # Multiplication
    mathparse.parse('шість помножити на дев'ять', language='UKR')
    >>> 54

    # Powers
    mathparse.parse('чотири у квадраті', language='UKR')
    >>> 16

Thai (THA)
++++++++++

.. code-block:: python

    # Basic arithmetic
    mathparse.parse('ห้า บวก สาม', language='THA')
    >>> 8

    # Multiplication
    mathparse.parse('หก คูณ เก้า', language='THA')
    >>> 54

    # Powers
    mathparse.parse('สี่ ยกกำลังสอง', language='THA')
    >>> 16

Simplified Chinese (CHI)
++++++++++++++++++++++++

.. code-block:: python

    # Basic arithmetic using Chinese characters
    mathparse.parse('五 加 三', language='CHI')
    >>> 8

    # Multiplication
    mathparse.parse('六 乘 九', language='CHI')
    >>> 54

    # Using alternative number representations
    mathparse.parse('五十 加上 二十', language='CHI')
    >>> 70

    # Large numbers with scales
    mathparse.parse('三 百 加 五十', language='CHI')
    >>> 350

    mathparse.parse('两 千 五 百', language='CHI')
    >>> 2500

    # Powers and roots
    mathparse.parse('四 平方', language='CHI')
    >>> 16

    mathparse.parse('平方根 十六', language='CHI')
    >>> 4.0

    # Negative numbers
    mathparse.parse('负 五 加 十', language='CHI')
    >>> 5

Common Operators by Language
----------------------------

English Operators
+++++++++++++++++

.. list-table:: English Mathematical Terms
   :widths: 30 20 50
   :header-rows: 1

   * - Operation
     - Operator
     - Example
   * - Addition
     - plus
     - ``'five plus three'``
   * - Subtraction
     - minus
     - ``'ten minus four'``
   * - Multiplication
     - times
     - ``'six times seven'``
   * - Division
     - divided by
     - ``'twenty divided by four'``
   * - Decimal Point
     - point
     - ``'five point two'``
   * - Power
     - to the power of
     - ``'two to the power of three'``
   * - Square
     - squared
     - ``'five squared'``
   * - Cube
     - cubed
     - ``'three cubed'``
   * - Square Root
     - square root of
     - ``'square root of nine'``
   * - Negative
     - negative
     - ``'negative five'``

French Operators
++++++++++++++++

.. list-table:: French Mathematical Terms
   :widths: 30 20 50
   :header-rows: 1

   * - Operation
     - Operator
     - Example
   * - Addition
     - plus
     - ``'cinq plus trois'``
   * - Subtraction
     - moins
     - ``'dix moins quatre'``
   * - Multiplication
     - fois
     - ``'six fois sept'``
   * - Division
     - divisé par
     - ``'vingt divisé par quatre'``
   * - Decimal Point
     - virgule
     - ``'cinq virgule deux'``
   * - Power
     - à la puissance
     - ``'deux à la puissance trois'``

Error Handling
--------------

When using language-specific parsing, mathparse will raise an ``InvalidLanguageCodeException`` if an unsupported language code is provided:

.. code-block:: python

    from mathparse import mathparse
    from mathparse.mathwords import InvalidLanguageCodeException

    try:
        result = mathparse.parse('five plus three', language='INVALID')
    except InvalidLanguageCodeException as e:
        print(f"Error: {e}")
        # Output: Error: INVALID is not an available language code

Mixed Language Support
----------------------

.. note::

    mathparse does not support mixing languages within a single expression. 
    Each expression must use terms from a single language.

    **Correct:**

    .. code-block:: python

        mathparse.parse('five plus three', language='ENG')  # All English
        mathparse.parse('cinq plus trois', language='FRE')  # All French

    **Incorrect:**

    .. code-block:: python

        # This will not work - mixing English and French
        mathparse.parse('five plus trois', language='ENG')
