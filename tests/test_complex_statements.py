from decimal import Decimal
from unittest import TestCase
from mathparse import mathparse


class ComplexStatementsTestCase(TestCase):
    """
    Test cases for complex mathematical expressions.
    """

    def test_numbers_with_spaces(self):
        result = mathparse.parse(
            'one hundred times fifty four', language='ENG'
        )
        self.assertEqual(result, 100 * 54)

    def test_numeric_values_with_squared_operator(self):
        result = mathparse.parse(
            '10 plus 2 squared times 3', language='ENG'
        )
        self.assertEqual(result, 10 + 2 ** 2 * 3)

    def test_numeric_values_with_square_root_operator(self):
        result = mathparse.parse(
            '10 plus the square root of 4 times 3',
            language='ENG',
            stopwords={'the'}
        )
        self.assertEqual(result, 10 + 2 * 3)

    def test_long_worded_number(self):
        result = mathparse.parse(
            'one thousand two hundred thirty four plus '
            'five thousand six hundred seventy eight',
            language='ENG'
        )
        self.assertEqual(result, 1234 + 5678)

    def test_invalid_expression(self):
        with self.assertRaises(mathparse.PostfixTokenEvaluationException) as e:
            mathparse.parse('two plus times three', language='ENG')

        self.assertEqual(
            str(e.exception),
            'Insufficient values in expression for operator "+"'
        )

    def test_unsupported_mathematical_term(self):
        with self.assertRaises(mathparse.PostfixTokenEvaluationException) as e:
            mathparse.parse('two squiggle eight', language='ENG')

        self.assertEqual(
            str(e.exception),
            'Unsupported mathematical term: "squiggle"'
        )

    def test_stopwords_contained_within_expressions(self):
        """
        Stopwords should not be removed if they are a part of a valid
        mathematical expression.
        """
        result = mathparse.parse(
            'the square root of four',
            language='ENG',
            stopwords={'the', 'of'}
        )
        self.assertEqual(result, 2)

    def test_unicode_pi_symbol(self):
        """
        Test using the unicode π symbol as a constant.
        """
        result = mathparse.parse('2 * π')
        self.assertAlmostEqual(result, 2 * 3.141593, places=5)

    def test_unicode_pi_in_expression(self):
        """
        Test using the unicode π symbol in a complex expression.
        """
        result = mathparse.parse('π + 1')
        self.assertAlmostEqual(result, 3.141593 + 1, places=5)

    def test_with_operations_and_single_numbers(self):
        """
        Test mixed integer and float operations in a complex expression.
        """
        result = mathparse.parse(
            "(1 + 3 + 2.0 + 6) * 0.00001"
        )
        self.assertEqual(result, Decimal('0.00012'))

    def test_mixed_decimal_and_float_operations(self):
        """
        Test arithmetic with Decimal and float operands in either order.
        """
        cases = {
            '1 / 2 + 0.25': 0.75,
            '0.25 + 1 / 2': 0.75,
            '1 / 2 - 0.25': 0.25,
            '0.25 - 1 / 2': -0.25,
            '1 / 2 * 0.25': 0.125,
            '0.25 * (1 / 2)': 0.125,
            '(1 / 2) ^ 0.5': 2 ** -0.5,
        }
        for expression, expected in cases.items():
            with self.subTest(expression=expression):
                self.assertAlmostEqual(float(mathparse.parse(expression)),
                                       expected)

    def test_numeric_result_types(self):
        """
        Preserve integer, float, and division result types.
        """
        self.assertIsInstance(mathparse.parse('2 ^ 100'), int)
        self.assertEqual(mathparse.parse('2 ^ 100'), 2 ** 100)
        self.assertIsInstance(mathparse.parse('1.5 + 2'), float)
        self.assertEqual(mathparse.parse('1 / 3'), Decimal(1) / Decimal(3))

    def test_expensive_powers_are_rejected(self):
        """
        Reject expensive powers before computing them.
        """
        expressions = (
            '9 ^ 999999', '9 ^ 9 ^ 9', '10 ^ 4000',
            '(10 / 1) ^ 4000', '0.1 ^ -10000',
            '2 ^ -10001', '9.5 ^ 500',
        )
        for expression in expressions:
            with self.subTest(expression=expression):
                with self.assertRaises(
                    mathparse.PostfixTokenEvaluationException
                ):
                    mathparse.parse(expression)

    def test_reasonable_powers_are_allowed(self):
        """
        Keep normal and moderately large powers available.
        """
        self.assertEqual(mathparse.parse('2 ^ 10'), 1024)
        self.assertEqual(mathparse.parse('2 ^ 10000'), 2 ** 10000)
        self.assertEqual(mathparse.parse('2 ^ -3'), 0.125)
        self.assertEqual(mathparse.parse('1.0 ^ 10000'), 1)
