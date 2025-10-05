from unittest import TestCase
from mathparse import mathparse


class SimplifiedChineseTestCase(TestCase):

    def test_addition_words(self):
        result = mathparse.parse('四加四', language='CHI')

        self.assertEqual(result, 8)

    def test_addition_words_large(self):
        result = mathparse.parse('四千两百一加五百', language='CHI')

        self.assertEqual(result, 4701)

    def test_subtraction_words(self):
        result = mathparse.parse('三十减二十', language='CHI')

        self.assertEqual(result, 10)

    def test_multiplication_words(self):
        result = mathparse.parse('九乘九', language='CHI')

        self.assertEqual(result, 81)

    def test_division_words(self):
        result = mathparse.parse('十五除以五', language='CHI')

        self.assertEqual(result, 3)

    def test_division_words_large(self):
        result = mathparse.parse('一千两百四除以一百', language='CHI')

        self.assertEqual(str(result), '12.04')

    def test_sqrt(self):
        result = mathparse.parse('四开方', language='CHI')

        self.assertEqual(result, 2)

    def test_squared(self):
        result = mathparse.parse('二平方', language='CHI')

        self.assertEqual(result, 4)

    def test_cubed(self):
        result = mathparse.parse('二立方', language='CHI')

        self.assertEqual(result, 8)
