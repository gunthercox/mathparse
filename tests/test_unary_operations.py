from unittest import TestCase
from mathparse import mathparse


class UnaryOperatorTestCase(TestCase):

    def test_exponent(self):
        result = mathparse.parse('4 ^ 4')

        self.assertEqual(result, 256)


class UnaryWordOperatorTestCase(TestCase):

    def test_sqrt(self):
        result = mathparse.parse('sqrt 4')

        self.assertEqual(result, 2)

    def test_sqrt_parenthesis(self):
        result = mathparse.parse('sqrt(4)')

        self.assertEqual(result, 2)

    def test_square_root(self):
        result = mathparse.parse('square root of 4', language='ENG')

        self.assertEqual(result, 2)