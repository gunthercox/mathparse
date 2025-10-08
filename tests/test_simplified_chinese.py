from unittest import TestCase
from mathparse import mathparse


class ChineseTestCase(TestCase):
    """
    Useful examples were noted for Mandarin language support in
    https://github.com/gunthercox/mathparse/issues/19

    NOTES:
        -2 + 2 in Mandarin statement could be '负二加二'.
        '负' means 'negative', '二' means 2 and '加' means 'plus'. The Mandarin
        language has almost the same grammar/order as English when stating a
        mathematical statement. For the basic four operators:
        plus, minus, multiplication and division, statements in Mandarin are
        always like 'a (positive/negative) number' + 'operator' +
        'a (positive/negative) number', similar to English.

        22 in Mandarin could be '二的平方'.
        '平方' means 'squares', and '的' is a necessary character that could be
        interpreted as 'whose'.
        For exponential statements in Mandarin, there is a general rule:
        22 —> '二的平方'
        32 —> '三的平方'
        42 —> '四的平方'
        Just replace the base number.
        Similarly for exponent of three:
        2^3 —> '二的立方'
        3^3 —> '三的立方'
        4^3 —> '四的立方'
        where '立方' is a specific word for exponent of three.
        But it becomes more regular for the exponent greater or equal to four.
        It would be:
        2^4 —> '二的四次方'  where '四' means 4
        2^5 —> '三的五次方' where '五' means 5
        2^10 —> '四的十次方' where '十' means 10
        Basically the rule becomes 'base number's exponent of n'.
        So actually only the exponent of 2 and 3 have their specific
        name ('平方','立方' respectively).
    """

    def test_addition_with_compound_statement(self):
        """
        二加二 is "two plus two" but no spaces are used between the characters.
        """
        result = mathparse.parse('二加二', language='CHI')
        self.assertEqual(result, 4)

    def test_addition(self):
        result = mathparse.parse('四 加 四', language='CHI')
        self.assertEqual(result, 8)

    def test_addition_with_negative_number(self):
        """
        负二加二 is "-2 plus 2", no spaces are used between the characters.
        """
        result = mathparse.parse('负二加二', language='CHI')
        self.assertEqual(result, 0)

    def test_compound_operators(self):
        """
        Test compound operators like 除以, 乘以, 加上
        """
        # Division with compound operator
        result = mathparse.parse('八 除以 二', language='CHI')
        self.assertEqual(result, 4)

        # Multiplication with compound operator
        result = mathparse.parse('三 乘以 五', language='CHI')
        self.assertEqual(result, 15)

        # Addition with compound operator
        result = mathparse.parse('十 加上 五', language='CHI')
        self.assertEqual(result, 15)

    def test_deconstructions(self):
        """
        Test Chinese 的 possessive constructions for powers.
        """
        # Square (specific name)
        result = mathparse.parse('三的平方', language='CHI')
        self.assertEqual(result, 9)

        # Cube (specific name)
        result = mathparse.parse('二的立方', language='CHI')
        self.assertEqual(result, 8)

        # General power construction
        result = mathparse.parse('二的四次方', language='CHI')
        self.assertEqual(result, 16)

        result = mathparse.parse('三的五次方', language='CHI')
        self.assertEqual(result, 243)

    def test_deconstructions_with_spaces(self):
        """
        Test Chinese 的 constructions with spaces.
        """
        result = mathparse.parse('二 的 四 次方', language='CHI')
        self.assertEqual(result, 16)

        result = mathparse.parse('三 的平方', language='CHI')
        self.assertEqual(result, 9)

    def test_prefix_unary_operators(self):
        """Test Chinese prefix operators like square root"""
        result = mathparse.parse('平方根 九', language='CHI')
        self.assertEqual(result, 3.0)

        result = mathparse.parse('开方 十六', language='CHI')
        self.assertEqual(result, 4.0)

    def test_postfix_unary_operators(self):
        """Test Chinese postfix operators without 的"""
        result = mathparse.parse('三 平方', language='CHI')
        self.assertEqual(result, 9)

        result = mathparse.parse('二 立方', language='CHI')
        self.assertEqual(result, 8)


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
