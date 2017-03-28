from unittest import TestCase
from mathparse import mathparse


class UnaryOperatorTestCase(TestCase):

    def test_exponent(self):
        result = mathparse.parse('4 ^ 4')

        self.assertEqual(result, 256)