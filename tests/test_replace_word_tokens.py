from unittest import TestCase
from mathparse import mathparse


class EnglishWordTokenTestCase(TestCase):

    def test_addition(self):
        result = mathparse.replace_word_tokens('1 plus 1', language='ENG')

        self.assertEqual(result, '1 + 1')

    def test_thirty(self):
        result = mathparse.replace_word_tokens(
            'thirty + thirty', language='ENG'
        )

        self.assertEqual(result, '30 + 30')

    def test_thousand(self):
        result = mathparse.replace_word_tokens(
            'five thousand + 30', language='ENG'
        )

        # Note: this ends up with double parentheses because it is both a
        # scaled number ("thousand") and a word group ("five thousand")
        self.assertEqual(result, '((5 * 1000)) + 30')

    def test_double_digit_multiplier_for_scale(self):
        result = mathparse.replace_word_tokens(
            'fifty thousand + 1', language='ENG'
        )

        self.assertEqual(result, '((50 * 1000)) + 1')
