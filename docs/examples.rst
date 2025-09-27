Examples and Use Cases
======================

This section provides comprehensive examples demonstrating mathparse functionality across different scenarios and use cases.

Basic Arithmetic Examples
--------------------------

Numeric Expressions
+++++++++++++++++++

.. code-block:: python

    from mathparse import mathparse

    # Basic operations
    result = mathparse.parse('2 + 3')
    print(result)  # 5

    result = mathparse.parse('10 - 4')
    print(result)  # 6

    result = mathparse.parse('6 * 7')
    print(result)  # 42

    result = mathparse.parse('20 / 4')
    print(result)  # 5.0

    result = mathparse.parse('2 ^ 3')
    print(result)  # 8

Order of Operations Examples
++++++++++++++++++++++++++++

.. code-block:: python

    # PEMDAS rules apply
    result = mathparse.parse('2 + 3 * 4')
    print(result)  # 14 (not 20)

    result = mathparse.parse('(2 + 3) * 4')
    print(result)  # 20

    result = mathparse.parse('2 ^ 3 * 4')
    print(result)  # 32

    result = mathparse.parse('(2 ^ 3) * 4')
    print(result)  # 32

    result = mathparse.parse('2 ^ (3 * 4)')
    print(result)  # 4096

Word-Based Expressions
----------------------

English Examples
++++++++++++++++

.. code-block:: python

    from mathparse import mathparse

    # Basic arithmetic in English
    result = mathparse.parse('five plus three', language='ENG')
    print(result)  # 8

    result = mathparse.parse('twenty minus seven', language='ENG')
    print(result)  # 13

    result = mathparse.parse('six times nine', language='ENG')
    print(result)  # 54

    result = mathparse.parse('forty divided by eight', language='ENG')
    print(result)  # 5.0

    # Complex expressions
    result = mathparse.parse('(five plus three) times two', language='ENG')
    print(result)  # 16

    result = mathparse.parse('fifty minus (ten times four)', language='ENG')
    print(result)  # 10

Large Numbers in English
++++++++++++++++++++++++

.. code-block:: python

    # Hundreds
    result = mathparse.parse('five hundred', language='ENG')
    print(result)  # 500

    result = mathparse.parse('three hundred twenty five', language='ENG')
    print(result)  # 325

    # Thousands
    result = mathparse.parse('two thousand', language='ENG')
    print(result)  # 2000

    result = mathparse.parse('four thousand five hundred', language='ENG')
    print(result)  # 4500

    result = mathparse.parse('ten thousand two hundred thirty', language='ENG')
    print(result)  # 10230

    # Millions and beyond
    result = mathparse.parse('one million', language='ENG')
    print(result)  # 1000000

    result = mathparse.parse('two million three hundred thousand', language='ENG')
    print(result)  # 2300000

    result = mathparse.parse('five billion', language='ENG')
    print(result)  # 5000000000

Multi-Language Examples
-----------------------

French Examples
+++++++++++++++

.. code-block:: python

    # Basic arithmetic in French
    result = mathparse.parse('cinq plus trois', language='FRE')
    print(result)  # 8

    result = mathparse.parse('vingt moins sept', language='FRE')
    print(result)  # 13

    result = mathparse.parse('six fois neuf', language='FRE')
    print(result)  # 54

    result = mathparse.parse('quarante divisé par huit', language='FRE')
    print(result)  # 5.0

    # Large numbers
    result = mathparse.parse('cinq cent', language='FRE')
    print(result)  # 500

    result = mathparse.parse('deux mille trois cent', language='FRE')
    print(result)  # 2300

German Examples
+++++++++++++++

.. code-block:: python

    # Basic arithmetic in German
    result = mathparse.parse('fünf plus drei', language='GER')
    print(result)  # 8

    result = mathparse.parse('zwanzig minus sieben', language='GER')
    print(result)  # 13

    result = mathparse.parse('sechs mal neun', language='GER')
    print(result)  # 54

    result = mathparse.parse('vierzig geteilt durch acht', language='GER')
    print(result)  # 5.0

    # Powers
    result = mathparse.parse('vier hoch zwei', language='GER')
    print(result)  # 16

    result = mathparse.parse('drei im Quadrat', language='GER')
    print(result)  # 9

Portuguese Examples
++++++++++++++++++++++

.. code-block:: python

    # Basic arithmetic in Portuguese
    result = mathparse.parse('cinco mais três', language='POR')
    print(result)  # 8

    result = mathparse.parse('vinte menos sete', language='POR')
    print(result)  # 13

    result = mathparse.parse('seis vezes nove', language='POR')
    print(result)  # 54

    result = mathparse.parse('quarenta dividido por oito', language='POR')
    print(result)  # 5.0

    # Powers and roots
    result = mathparse.parse('quatro ao quadrado', language='POR')
    print(result)  # 16

    result = mathparse.parse('raiz quadrada de dezesseis', language='POR')
    print(result)  # 4.0

Advanced Mathematical Functions
-------------------------------

Constants and Functions
+++++++++++++++++++++++

.. code-block:: python

    # Mathematical constants
    result = mathparse.parse('pi')
    print(result)  # 3.141693

    result = mathparse.parse('e')
    print(result)  # 2.718281

    result = mathparse.parse('pi * 2')
    print(result)  # 6.283386

    result = mathparse.parse('e ^ 2')
    print(result)  # 7.389056

    # Functions
    result = mathparse.parse('sqrt 16')
    print(result)  # 4.0

    result = mathparse.parse('sqrt 25')
    print(result)  # 5.0

    result = mathparse.parse('log 100')
    print(result)  # 2.0

    result = mathparse.parse('log 1000')
    print(result)  # 3.0

Complex Expressions with Functions
++++++++++++++++++++++++++++++++++

.. code-block:: python

    # Combining functions with arithmetic
    result = mathparse.parse('sqrt 16 + 3')
    print(result)  # 7.0

    result = mathparse.parse('(sqrt 9) * 5')
    print(result)  # 15.0

    result = mathparse.parse('log 100 * pi')
    print(result)  # 6.283386

    # Nested functions and constants
    result = mathparse.parse('sqrt (pi * 4)')
    print(result)  # 3.5449074

    result = mathparse.parse('(log 100) ^ 2')
    print(result)  # 4.0

    # Complex expressions
    result = mathparse.parse('sqrt ((3 + 4) ^ 2)')
    print(result)  # 7.0

Word-Based Function Examples
++++++++++++++++++++++++++++

.. code-block:: python

    # English function words
    result = mathparse.parse('square root of sixteen', language='ENG')
    print(result)  # 4.0

    result = mathparse.parse('four squared', language='ENG')
    print(result)  # 16

    result = mathparse.parse('three cubed', language='ENG')
    print(result)  # 27

    result = mathparse.parse('two to the power of five', language='ENG')
    print(result)  # 32

    # Combining with other operations
    result = mathparse.parse('square root of sixteen plus five', language='ENG')
    print(result)  # 9.0

    result = mathparse.parse('three squared times two', language='ENG')
    print(result)  # 18

Practical Use Cases
-------------------

Calculator Application
++++++++++++++++++++++

.. code-block:: python

    from mathparse import mathparse
    from mathparse.mathwords import InvalidLanguageCodeException
    from mathparse.mathparse import PostfixTokenEvaluationException

    def calculator(expression, language=None):
        """A simple calculator function using mathparse."""
        try:
            result = mathparse.parse(expression, language=language)
            if result == 'undefined':
                return "Error: Division by zero"
            return f"Result: {result}"
        except InvalidLanguageCodeException:
            return "Error: Unsupported language"
        except PostfixTokenEvaluationException:
            return "Error: Invalid expression"
        except Exception as e:
            return f"Error: {str(e)}"

    # Test the calculator
    print(calculator('2 + 3 * 4'))
    # Output: Result: 14

    print(calculator('five plus three', language='ENG'))
    # Output: Result: 8

    print(calculator('10 / 0'))
    # Output: Error: Division by zero

    print(calculator('invalid expression'))
    # Output: Error: Invalid expression

Natural Language Processing
+++++++++++++++++++++++++++

.. code-block:: python

    def extract_and_calculate(sentence, language='ENG'):
        """Extract and solve mathematical expressions from sentences."""
        try:
            # Extract the mathematical expression
            expression = mathparse.extract_expression(sentence, language)
            
            # Parse and calculate
            result = mathparse.parse(expression, language=language)
            
            return {
                'original': sentence,
                'extracted': expression,
                'result': result
            }
        except Exception as e:
            return {
                'original': sentence,
                'error': str(e)
            }

    # Examples
    result = extract_and_calculate("What is five plus three?")
    print(result)
    # Output: {'original': 'What is five plus three?', 
    #          'extracted': 'five plus three', 
    #          'result': 8}

    result = extract_and_calculate("Calculate two times seven minus one")
    print(result)
    # Output: {'original': 'Calculate two times seven minus one', 
    #          'extracted': 'two times seven minus one', 
    #          'result': 13}

Unit Conversion Helper
++++++++++++++++++++++

.. code-block:: python

    def convert_units():
        """Examples of using mathparse for unit conversions."""
        
        # Temperature conversion: Celsius to Fahrenheit
        # F = C * 9/5 + 32
        celsius = 25
        fahrenheit = mathparse.parse(f'{celsius} * 9 / 5 + 32')
        print(f"{celsius}°C = {fahrenheit}°F")  # 25°C = 77.0°F
        
        # Area of circle: π * r²
        radius = 5
        area = mathparse.parse(f'pi * {radius} * {radius}')
        print(f"Circle area (r={radius}): {area}")  # Circle area (r=5): 78.54225
        
        # Compound interest: P * (1 + r)^t
        principal = 1000
        rate = 0.05  # 5%
        time = 3
        amount = mathparse.parse(f'{principal} * (1 + {rate}) ^ {time}')
        print(f"Compound interest: ${amount}")  # Compound interest: $1157.625

Educational Applications
++++++++++++++++++++++++

.. code-block:: python

    def math_quiz():
        """Create a simple math quiz using word problems."""
        questions = [
            ("What is five plus seven?", 'ENG', 12),
            ("Calculate three times four minus two", 'ENG', 10),
            ("Find square root of twenty five", 'ENG', 5.0),
            ("What is deux plus trois?", 'FRE', 5),  # French
            ("Calculate fünf mal sechs", 'GER', 30),  # German
        ]
        
        for question, lang, expected in questions:
            try:
                # Extract and solve
                expression = mathparse.extract_expression(question, lang)
                result = mathparse.parse(expression, language=lang)
                
                correct = "✓" if result == expected else "✗"
                print(f"{correct} {question}")
                print(f"   Expression: {expression}")
                print(f"   Answer: {result}")
                print()
            except Exception as e:
                print(f"✗ {question}")
                print(f"   Error: {e}")
                print()

    # Run the quiz
    math_quiz()

Error Handling Examples
-----------------------

Common Error Scenarios
++++++++++++++++++++++

.. code-block:: python

    from mathparse import mathparse
    from mathparse.mathwords import InvalidLanguageCodeException
    from mathparse.mathparse import PostfixTokenEvaluationException

    # Division by zero
    result = mathparse.parse('10 / 0')
    print(result)  # 'undefined'

    # Invalid language code
    try:
        result = mathparse.parse('five plus three', language='INVALID')
    except InvalidLanguageCodeException as e:
        print(f"Language error: {e}")
        # Output: Language error: INVALID is not an available language code

    # Invalid expression
    try:
        result = mathparse.parse('5 & 3')  # & is not a valid operator
    except PostfixTokenEvaluationException as e:
        print(f"Expression error: {e}")

    # Empty expression
    try:
        result = mathparse.parse('')
    except PostfixTokenEvaluationException as e:
        print(f"Empty expression error: {e}")

Robust Error Handling
+++++++++++++++++++++

.. code-block:: python

    def safe_parse(expression, language=None, default=None):
        """Safely parse expressions with comprehensive error handling."""
        try:
            result = mathparse.parse(expression, language=language)
            
            # Check for division by zero
            if result == 'undefined':
                return {'success': False, 'error': 'Division by zero', 'result': default}
            
            return {'success': True, 'result': result}
            
        except InvalidLanguageCodeException:
            return {'success': False, 'error': 'Invalid language code', 'result': default}
        except PostfixTokenEvaluationException as e:
            return {'success': False, 'error': f'Evaluation error: {e}', 'result': default}
        except Exception as e:
            return {'success': False, 'error': f'Unexpected error: {e}', 'result': default}

    # Examples
    print(safe_parse('2 + 3'))
    # Output: {'success': True, 'result': 5}

    print(safe_parse('10 / 0', default=0))
    # Output: {'success': False, 'error': 'Division by zero', 'result': 0}

    print(safe_parse('five plus three', language='INVALID', default=0))
    # Output: {'success': False, 'error': 'Invalid language code', 'result': 0}

Performance Examples
--------------------------

Benchmarking Example
++++++++++++++++++++

.. code-block:: python

    import time
    from mathparse import mathparse

    def benchmark_parsing():
        """Compare performance of numeric vs word-based parsing."""
        
        # Numeric expressions (faster)
        start_time = time.time()
        for i in range(1000):
            result = mathparse.parse('2 + 3 * 4')
        numeric_time = time.time() - start_time
        
        # Word-based expressions (slower due to text processing)
        start_time = time.time()
        for i in range(1000):
            result = mathparse.parse('two plus three times four', language='ENG')
        word_time = time.time() - start_time
        
        print(f"Numeric parsing: {numeric_time:.4f}s for 1000 operations")
        print(f"Word-based parsing: {word_time:.4f}s for 1000 operations")
        print(f"Word-based is {word_time/numeric_time:.1f}x slower")

    # Run benchmark
    benchmark_parsing()

Optimization Tips
+++++++++++++++++

.. code-block:: python

    # Use numeric expressions when possible for better performance
    fast_result = mathparse.parse('2 + 3')  # Faster

    # Instead of:
    slow_result = mathparse.parse('two plus three', language='ENG')  # Slower

    # Cache language validation for repeated operations
    from mathparse.mathwords import word_groups_for_language

    # Pre-validate language once
    try:
        language_words = word_groups_for_language('ENG')
        # Now you can safely use 'ENG' multiple times
        for expression in ['five plus three', 'ten minus four', 'six times seven']:
            result = mathparse.parse(expression, language='ENG')
            print(result)
    except InvalidLanguageCodeException:
        print("Invalid language code")

    # For batch processing, validate expressions first
    def batch_parse(expressions, language=None):
        """Parse multiple expressions efficiently."""
        results = []
        
        # Pre-validate language if provided
        if language:
            try:
                word_groups_for_language(language)
            except InvalidLanguageCodeException:
                return [{'error': 'Invalid language code'}] * len(expressions)
        
        # Process all expressions
        for expr in expressions:
            try:
                result = mathparse.parse(expr, language=language)
                results.append({'success': True, 'result': result})
            except Exception as e:
                results.append({'success': False, 'error': str(e)})
        
        return results

    # Example usage
    expressions = ['2 + 3', '10 * 5', '100 / 4']
    results = batch_parse(expressions)
    for i, result in enumerate(results):
        print(f"Expression {i+1}: {result}")
