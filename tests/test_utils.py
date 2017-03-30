from unittest import TestCase
from mathparse import mathparse


class ExtractExpressionTestCase(TestCase):

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
        result = mathparse.extract_expression('What is three plus three?', language='ENG')

        self.assertEqual(result, 'three plus three')