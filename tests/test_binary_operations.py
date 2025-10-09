from unittest import TestCase
from mathparse import mathparse


class PositiveIntegerTestCase(TestCase):

    def test_addition(self):
        result = mathparse.parse('4 + 4')

        self.assertEqual(result, 8)

    def test_addition_words(self):
        result = mathparse.parse('four plus four', language='ENG')

        self.assertEqual(result, 8)

    def test_addition_words_large(self):
        result = mathparse.parse(
            'four thousand two hundred one plus five hundred', language='ENG'
        )

        self.assertEqual(result, 4701)

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

    def test_double_digit_multiplier_for_scale_addition(self):
        result = mathparse.parse('fifty thousand plus one', language='ENG')

        self.assertEqual(result, 50001)

    def test_division_by_zero(self):
        result = mathparse.parse('42 / 0', language='ENG')

        self.assertEqual(result, 'undefined')

    def test_division_by_zero_words(self):
        result = mathparse.parse('six divided by zero', language='ENG')

        self.assertEqual(result, 'undefined')

    def test_division_words_large(self):
        result = mathparse.parse(
            'one thousand two hundred four divided by one hundred',
            language='ENG'
        )

        self.assertEqual(str(result), '12.04')

    def test_operation_precedence(self):
        result = mathparse.parse('2 + 3 * (4 - 2) ^ 2 / 2')

        self.assertEqual(result, 8)

    def test_tokens_with_extra_spaces(self):
        result = mathparse.parse('  2   +    3   * (  4 - 2 ) ^ 2 / 2  ')

        self.assertEqual(result, 8)

    def test_tokens_with_no_spaces(self):
        result = mathparse.parse('2+3*(4-2)^2/2')

        self.assertEqual(result, 8)


class PositiveFloatTestCase(TestCase):

    def test_addition(self):
        result = mathparse.parse('0.6 + 0.5')

        self.assertEqual(result, 1.1)

    def test_subtraction(self):
        result = mathparse.parse('30.1 - 29.1')

        self.assertEqual(result, 1)

    def test_multiplication(self):
        result = mathparse.parse('0.9 * 0.9')

        self.assertEqual(result, 0.81)

    def test_division(self):
        result = mathparse.parse('0.6 / 0.2')

        self.assertEqual(result, 3)


class WordOperatorTestCase(TestCase):

    def test_power_of(self):
        result = mathparse.parse('2 to the power of 3', language='ENG')

        self.assertEqual(result, 8)


class WordBasedDecimalTestCase(TestCase):
    """
    Test cases for word-based decimal numbers.
    For example: "fifty three point four" should be treated as 53.4
    """

    def test_word_decimal_with_multiplication(self):
        """
        Test: "Fifty three point four times seven" should equal 53.4 * 7
        """
        result = mathparse.parse(
            'fifty three point four times seven', language='ENG'
        )

        self.assertEqual(result, 53.4 * 7)

    def test_word_decimal_simple(self):
        """
        Test: "five point two" should equal 5.2
        """
        result = mathparse.parse('five point two', language='ENG')

        self.assertEqual(result, 5.2)

    def test_word_decimal_with_addition(self):
        """
        Test: "three point five plus two point one" should equal 5.6
        """
        result = mathparse.parse(
            'three point five plus two point one', language='ENG'
        )

        self.assertEqual(result, 5.6)

    def test_word_decimal_with_division(self):
        """
        Test: "twenty one point six divided by four" should equal 5.4
        """
        result = mathparse.parse(
            'twenty one point six divided by four', language='ENG'
        )

        self.assertEqual(float(result), 5.4)

    def test_word_decimal_multi_digit_fractional(self):
        """
        Test: "ten point twenty five" should equal 10.25
        """
        result = mathparse.parse('ten point twenty five', language='ENG')

        self.assertEqual(result, 10.25)
