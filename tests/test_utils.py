from unittest import TestCase
from mathparse import mathparse
from mathparse.mathwords import InvalidLanguageCodeException


class BooleanChecksTestCase(TestCase):

    def test_is_integer(self):
        self.assertTrue(mathparse.is_int('42'))

    def test_is_not_integer(self):
        self.assertFalse(mathparse.is_int('42.2'))

    def test_is_float(self):
        self.assertTrue(mathparse.is_float('0.5'))

    def test_is_not_float(self):
        self.assertFalse(mathparse.is_float('5'))

    def test_is_constant(self):
        self.assertTrue(mathparse.is_constant('pi'))

    def test_is_not_constant(self):
        self.assertFalse(mathparse.is_constant('+'))

    def test_is_unary(self):
        self.assertTrue(mathparse.is_unary('sqrt'))

    def test_is_not_unary(self):
        self.assertFalse(mathparse.is_unary('+'))

    def test_is_binary(self):
        self.assertTrue(mathparse.is_binary('-'))

    def test_is_not_binary(self):
        self.assertFalse(mathparse.is_binary('sqrt'))

    def test_is_word(self):
        self.assertTrue(mathparse.is_word('three', language='ENG'))

    def test_is_not_word(self):
        self.assertFalse(mathparse.is_word('3', language='ENG'))


class TokenizationTestCase(TestCase):

    def test_lowercase_tokens(self):
        result = mathparse.tokenize('Three PLUS five', language='ENG')

        self.assertEqual(result, ['three', 'plus', 'five'])

    def test_tokenize_invalid_language(self):
        with self.assertRaises(InvalidLanguageCodeException):
            mathparse.tokenize('Three PLUS five', language='123')

    def test_load_english_words(self):
        from mathparse import mathwords

        words = mathwords.words_for_language('ENG')
        self.assertIn('three', words)

    def test_load_nonexistent_data(self):
        from mathparse import mathwords

        with self.assertRaises(mathwords.InvalidLanguageCodeException):
            mathwords.words_for_language('&&&')


class ExtractExpressionTestCase(TestCase):

    def test_empty_string(self):
        result = mathparse.extract_expression('', language='ENG')

        self.assertEqual(result, '')

    def test_extract_expression(self):
        result = mathparse.extract_expression('3 + 3', language='ENG')

        self.assertEqual(result, '3 + 3')

    def test_ignore_punctuation(self):
        result = mathparse.extract_expression('3?', language='ENG')

        self.assertEqual(result, '3')

    def test_extract_expression_simple_additon(self):
        result = mathparse.extract_expression('What is 3 + 3?', language='ENG')

        self.assertEqual(result, '3 + 3')

    def test_extract_expression_simple_additon_words(self):
        result = mathparse.extract_expression(
            'What is three plus three?', language='ENG'
        )

        self.assertEqual(result, 'three plus three')
