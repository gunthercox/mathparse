from unittest import TestCase
from mathparse import mathparse


class ComplexStatementsTestCase(TestCase):
    """
    Test cases for complex mathematical expressions.
    """

    def test_numeric_values_with_squared_operator(self):
        result = mathparse.parse(
            '10 plus 2 squared times 3', language='ENG'
        )
        self.assertEqual(result, 10 + 2 ** 2 * 3)

    def test_numeric_values_with_square_root_operator(self):
        result = mathparse.parse(
            '10 plus square root of 4 times 3', language='ENG'
        )
        self.assertEqual(result, 10 + 2 * 3)
