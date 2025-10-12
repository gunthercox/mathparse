from unittest import TestCase
from mathparse import mathparse


class NegativeNumberTestCase(TestCase):
    """
    Test cases for basic negative number operations.
    """

    def test_leading_negative_with_addition(self):
        """
        Test: -3 + 3 should equal 0
        """
        result = mathparse.parse('-3 + 3')
        self.assertEqual(result, 0)

    def test_leading_negative_with_subtraction(self):
        """
        Test: -3 - 5 should equal -8
        """
        result = mathparse.parse('-3 - 5')
        self.assertEqual(result, -8)

    def test_leading_negative_with_multiplication(self):
        """
        Test: -10 * 2 should equal -20
        """
        result = mathparse.parse('-10 * 2')
        self.assertEqual(result, -20)

    def test_negative_in_parentheses(self):
        """
        Test: (-3) should equal -3
        """
        result = mathparse.parse('(-3)')
        self.assertEqual(result, -3)

    def test_negative_in_parentheses_with_addition(self):
        """
        Test: (-3) + 5 should equal 2
        """
        result = mathparse.parse('(-3) + 5')
        self.assertEqual(result, 2)

    def test_addition_with_negative_in_parentheses(self):
        """
        Test: 5 + (-3) should equal 2
        """
        result = mathparse.parse('5 + (-3)')
        self.assertEqual(result, 2)

    def test_two_negatives_in_parentheses(self):
        """
        Test: (-3) * (-2) should equal 6
        """
        result = mathparse.parse('(-3) * (-2)')
        self.assertEqual(result, 6)

    def test_multiplication_by_negative(self):
        """
        Test: 3 * -2 should equal -6
        """
        result = mathparse.parse('3 * -2')
        self.assertEqual(result, -6)

    def test_subtraction_of_negative(self):
        """
        Test: 3 - -2 should equal 5 (subtracting a negative)
        """
        result = mathparse.parse('3--2')
        self.assertEqual(result, 5)

    def test_two_separate_negatives_with_addition(self):
        """
        Test: -3 + -5 should equal -8
        """
        result = mathparse.parse('-3 + -5')
        self.assertEqual(result, -8)

    def test_complex_expression_with_leading_negative(self):
        """
        Test: (-3 + 5) * 2 should equal 4
        """
        result = mathparse.parse('(-3 + 5) * 2')
        self.assertEqual(result, 4)

    def test_negative_after_operator_in_expression(self):
        """
        Test: 2 * (-3 + 5) should equal 4
        """
        result = mathparse.parse('2 * (-3 + 5)')
        self.assertEqual(result, 4)

    def test_negative_of_expression(self):
        """
        Test: -(3 + 5) should equal -8
        """
        result = mathparse.parse('-(3 + 5)')
        self.assertEqual(result, -8)

    def test_negative_decimal(self):
        """
        Test: -3.5 should equal -3.5 (parsed as -3 . 5)
        """
        result = mathparse.parse('-3.5')
        self.assertEqual(float(result), -3.5)

    def test_negative_decimal_in_expression(self):
        """
        Test: -10.25 + 5 should work correctly
        """
        result = mathparse.parse('-10.25 + 5')
        # Parses as (-10) . 25 + 5 = -10.25 + 5 = -5.25
        self.assertEqual(float(result), -5.25)

    def test_positive_decimal(self):
        """
        Test: 3.5 should equal 3.5
        """
        result = mathparse.parse('3.5')
        self.assertEqual(float(result), 3.5)

    def test_negative_decimal_with_multiple_digits(self):
        """
        Test: -53.25 should equal -53.25
        """
        result = mathparse.parse('-53.25')
        self.assertEqual(float(result), -53.25)

    def test_negative_decimal_in_multiplication(self):
        """
        Test: -2.5 * 4 should equal -10.0
        """
        result = mathparse.parse('-2.5 * 4')
        self.assertEqual(float(result), -10.0)


class NegativeWithUnaryFunctionsTestCase(TestCase):
    """
    Test cases for negative numbers with unary functions.
    """

    def test_sqrt_with_negative_causes_math_error(self):
        """
        Test: sqrt -16 should parse correctly but give a math domain error.

        The tokenizer keeps -16 as a single token '-16', which is correctly
        identified as an integer and passed to sqrt, causing the expected
        math domain error.
        """
        # Verify tokenization
        tokens = mathparse.tokenize('sqrt -16')
        self.assertEqual(tokens, ['sqrt', '-16'])

        # Verify it causes the expected math error
        with self.assertRaises(ValueError) as context:
            mathparse.parse('sqrt -16')
        self.assertIn("math domain error", str(context.exception).lower())

    def test_log_with_negative_causes_math_error(self):
        """
        Test: log -10 should parse correctly but give a math domain error.
        """
        # Verify tokenization
        tokens = mathparse.tokenize('log -10')
        self.assertEqual(tokens, ['log', '-10'])

        # Verify it causes the expected math error
        with self.assertRaises(ValueError) as context:
            mathparse.parse('log -10')
        self.assertIn("math domain error", str(context.exception).lower())

    def test_sqrt_with_positive_after_operator(self):
        """
        Test: 3 + sqrt 16 should equal 7.0
        """
        result = mathparse.parse('3 + sqrt 16')
        self.assertEqual(result, 7.0)

    def test_multiple_negatives_with_operations(self):
        """
        Test: -2 * -3 + -1 should equal 5
        """
        result = mathparse.parse('-2 * -3 + -1')
        self.assertEqual(result, 5)


class ExtractExpressionNegativeTestCase(TestCase):
    """
    Test cases for extract_expression with negative numbers.
    """

    def test_extract_leading_negative(self):
        """
        Test: 'What is -3 + 3?' should extract '-3 + 3'
        """
        result = mathparse.extract_expression(
            'What is -3 + 3?', language='ENG'
        )
        self.assertEqual(result, '-3 + 3')

    def test_extract_negative_with_multiplication(self):
        """
        Test: 'Calculate -5 * 2' should extract '-5 * 2'
        """
        result = mathparse.extract_expression(
            'Calculate -5 * 2', language='ENG'
        )
        self.assertEqual(result, '-5 * 2')

    def test_extract_binary_subtraction(self):
        """
        Test: 'The answer to 10 - 5 is' should extract '10 - 5'
        """
        result = mathparse.extract_expression(
            'The answer to 10 - 5 is', language='ENG'
        )
        self.assertEqual(result, '10 - 5')

    def test_extract_pure_negative_expression(self):
        """
        Test: '-3 + 3' should extract '-3 + 3' (with no extra text)
        """
        result = mathparse.extract_expression('-3 + 3', language='ENG')
        self.assertEqual(result, '-3 + 3')

    def test_extract_pure_subtraction(self):
        """
        Test: '5 - 3' should extract '5 - 3' (with no extra text)
        """
        result = mathparse.extract_expression('5 - 3', language='ENG')
        self.assertEqual(result, '5 - 3')

    def test_extract_negative_decimal(self):
        """
        Test: Extract leading negative decimal from sentence
        """
        result = mathparse.extract_expression(
            'What is -100.5 * 20?', language='ENG'
        )
        self.assertEqual(result, '-100.5 * 20')

    def test_extract_negative_in_parentheses_with_words(self):
        """
        Test: Extract expression with negative in parentheses from sentence
        """
        result = mathparse.extract_expression(
            'Compute (-3) + 5', language='ENG'
        )
        # NOTE: Spaces are currently added, but ideally these will be removed
        # in the future
        self.assertEqual(result, '( -3 ) + 5')


class NegativeDecimalsLessThanOneTestCase(TestCase):
    """
    Test cases for negative decimal numbers between -1 and 0.

    This addresses a bug where negative decimals less than 1
    (e.g., -0.2, -0.5) were losing their negative sign during parsing.
    The issue was caused by Python's -0 == 0 equality, where int('-0')
    returns 0, losing sign information.
    """

    def test_negative_zero_point_two(self):
        """
        Test: -0.2 should equal -0.2
        """
        result = mathparse.parse('-0.2')
        self.assertEqual(result, -0.2)

    def test_negative_zero_point_five(self):
        """
        Test: -0.5 should equal -0.5
        """
        result = mathparse.parse('-0.5')
        self.assertEqual(result, -0.5)

    def test_negative_zero_point_nine(self):
        """
        Test: -0.9 should equal -0.9
        """
        result = mathparse.parse('-0.9')
        self.assertEqual(result, -0.9)

    def test_negative_zero_point_one(self):
        """
        Test: -0.1 should equal -0.1
        """
        result = mathparse.parse('-0.1')
        self.assertEqual(result, -0.1)

    def test_negative_zero_point_ninety_nine(self):
        """
        Test: -0.99 should equal -0.99"""
        result = mathparse.parse('-0.99')
        self.assertEqual(result, -0.99)

    def test_negative_zero_point_zero_one(self):
        """
        Test: -0.01 should equal -0.01
        """
        result = mathparse.parse('-0.01')
        self.assertEqual(result, -0.01)

    def test_negative_zero_point_nine_nine_nine(self):
        """
        Test: -0.999 should equal -0.999
        """
        result = mathparse.parse('-0.999')
        self.assertEqual(result, -0.999)

    def test_negative_decimal_in_addition(self):
        """
        Test: -0.5 + 1 should equal 0.5
        """
        result = mathparse.parse('-0.5 + 1')
        self.assertEqual(result, 0.5)

    def test_negative_decimal_in_subtraction(self):
        """
        Test: 2 - -0.5 should equal 2.5
        """
        result = mathparse.parse('2 - -0.5')
        self.assertEqual(result, 2.5)

    def test_negative_decimal_in_multiplication(self):
        """
        Test: -0.5 * 4 should equal -2.0
        """
        result = mathparse.parse('-0.5 * 4')
        self.assertEqual(result, -2.0)

    def test_negative_decimal_in_division(self):
        """
        Test: -0.8 / 2 should equal -0.4
        """
        result = mathparse.parse('-0.8 / 2')
        self.assertEqual(float(result), -0.4)

    def test_multiple_negative_decimals(self):
        """
        Test: -0.3 + -0.2 should equal -0.5
        """
        result = mathparse.parse('-0.3 + -0.2')
        self.assertAlmostEqual(result, -0.5, places=10)

    def test_negative_decimal_with_parentheses(self):
        """
        Test: (-0.5) should equal -0.5
        """
        result = mathparse.parse('(-0.5)')
        self.assertEqual(result, -0.5)

    def test_negative_decimal_in_complex_expression(self):
        """
        Test: (-0.5 + 1) * 2 should equal 1.0
        """
        result = mathparse.parse('(-0.5 + 1) * 2')
        self.assertEqual(result, 1.0)

    def test_positive_decimals_still_work(self):
        """
        Test: 0.5 should equal 0.5
        """
        result = mathparse.parse('0.5')
        self.assertEqual(result, 0.5)

    def test_negative_integers_still_work(self):
        """
        Test: -5 should equal -5
        """
        result = mathparse.parse('-5')
        self.assertEqual(result, -5)

    def test_negative_decimals_greater_than_one_still_work(self):
        """
        Test: -1.5 should equal -1.5
        """
        result = mathparse.parse('-1.5')
        self.assertEqual(result, -1.5)

    def test_temperature_conversion_use_case(self):
        """
        -0.2 Celsius to Fahrenheit formula: (-0.2 * 9/5) + 32 = 31.64
        (Example calculation)
        """
        result = mathparse.parse('-0.2 * 9 / 5 + 32')
        self.assertAlmostEqual(float(result), 31.64, places=2)

    def test_financial_calculation_use_case(self):
        """
        Balance: $100, transaction: -$0.25, expected: $99.75
        (Example calculation)
        """
        result = mathparse.parse('100 + -0.25')
        self.assertEqual(result, 99.75)
