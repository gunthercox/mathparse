from unittest import TestCase
from mathparse import mathparse


class PositiveIntegerTestCase(TestCase):

    def test_addition(self):
        result = mathparse.parse('4 + 4')

        self.assertEqual(result, 8)

    def test_addition_words(self):
        result = mathparse.parse('four plus four', language='ENG')

        self.assertEqual(result, 8)

    def test_subtraction(self):
        result = mathparse.parse('30 - 20')

        self.assertEqual(result, 10)

    def test_subtraction_words(self):
        result = mathparse.parse('thirty minus twenty', language='ENG')

        self.assertEqual(result, 10)

    def test_multiplication(self):
        result = mathparse.parse('9 * 9')

        self.assertEqual(result, 81)

    def test_multiplication_words(self):
        result = mathparse.parse('nine times nine', language='ENG')

        self.assertEqual(result, 81)

    def test_division(self):
        result = mathparse.parse('15 / 5')

        self.assertEqual(result, 3)

    def test_division_words(self):
        result = mathparse.parse('fifteen divided by five', language='ENG')

        self.assertEqual(result, 3)


class PositiveFloatTestCase(TestCase):

    def test_addition(self):
        result = mathparse.parse('0.6 + 0.5')

        self.assertEqual(result, 1.1)

    def test_subtraction(self):
        result = mathparse.parse('30 - 29')

        self.assertEqual(result, 1)

    def test_multiplication(self):
        result = mathparse.parse('0.9 * 0.9')

        self.assertEqual(result, 0.81)

    def test_division(self):
        result = mathparse.parse('0.6 / 0.2')

        self.assertEqual(result, 3)
