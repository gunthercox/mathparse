# -*- coding: utf-8 -*-
from unittest import TestCase
from mathparse import mathparse


class UnaryOperatorTestCase(TestCase):

    def test_exponent(self):
        result = mathparse.parse('4 ^ 4')

        self.assertEqual(result, 256)

    def test_without_unary_operator_fre(self):
        result = mathparse.parse('50 * (85 / 100)', language='FRE')
        self.assertEqual(result, 42.5)

    def test_without_unary_operator_rus(self):
        result = mathparse.parse('четыре плюс четыре',
                                 language='RUS')
        self.assertEqual(result, 8)


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

    def test_negative_number(self):
        result = mathparse.parse('-4 + 2')

        self.assertEqual(result, -2)
