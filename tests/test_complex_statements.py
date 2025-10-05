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
