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

    def test_square_root_with_decimal(self):
        result = mathparse.parse('sqrt(4) . 5')

        # TODO: Should this raise a parsing error instead of
        # returning a number (2.5)?

        raise self.skipTest('Skip until decision is made on expected behavior')

    def test_negative_number(self):
        result = mathparse.parse('-4 + 2')

        self.assertEqual(result, -2)

    def test_log_symbolic(self):
        result = mathparse.parse('log 100')

        self.assertEqual(result, 2.0)

    def test_log_symbolic_with_parenthesis(self):
        result = mathparse.parse('log(1000)')

        self.assertEqual(result, 3.0)

    def test_log_english(self):
        result = mathparse.parse('logarithm of 100', language='ENG')

        self.assertEqual(result, 2.0)

    def test_log_of_english(self):
        result = mathparse.parse('log of 1000', language='ENG')

        self.assertEqual(result, 3.0)

    def test_log_french(self):
        result = mathparse.parse('logarithme de 100', language='FRE')

        self.assertEqual(result, 2.0)

    def test_log_german(self):
        result = mathparse.parse('Logarithmus von 100', language='GER')

        self.assertEqual(result, 2.0)

    def test_log_spanish(self):
        result = mathparse.parse('logaritmo de 100', language='ESP')

        self.assertEqual(result, 2.0)

    def test_log_italian(self):
        result = mathparse.parse('logaritmo di 100', language='ITA')

        self.assertEqual(result, 2.0)

    def test_log_portuguese(self):
        result = mathparse.parse('logaritmo de 100', language='POR')

        self.assertEqual(result, 2.0)

    def test_log_russian(self):
        result = mathparse.parse('логарифм 100', language='RUS')

        self.assertEqual(result, 2.0)

    def test_log_ukrainian(self):
        result = mathparse.parse('логарифм 100', language='UKR')

        self.assertEqual(result, 2.0)

    def test_log_dutch(self):
        result = mathparse.parse('logaritme van 100', language='DUT')

        self.assertEqual(result, 2.0)

    def test_log_greek(self):
        result = mathparse.parse('λογάριθμος του 100', language='GRE')

        self.assertEqual(result, 2.0)

    def test_log_thai(self):
        result = mathparse.parse('ลอการิทึม 100', language='THA')

        self.assertEqual(result, 2.0)

    def test_log_chinese(self):
        result = mathparse.parse('对数 100', language='CHI')

        self.assertEqual(result, 2.0)

    def test_log_marathi(self):
        result = mathparse.parse('लॉगरिथम 100', language='MAR')

        self.assertEqual(result, 2.0)

    def test_log_in_expression(self):
        result = mathparse.parse('log 100 * 2')

        self.assertEqual(result, 4.0)

    def test_log_with_addition(self):
        result = mathparse.parse('log 100 + log 1000')

        self.assertEqual(result, 5.0)

    def test_log_with_power(self):
        result = mathparse.parse('(log 100) ^ 2')

        self.assertEqual(result, 4.0)
