from unittest import TestCase
from mathparse import mathparse
from mathparse.mathwords import InvalidLanguageCodeException


class LanguageSupportTestCase(TestCase):

    def test_unsupported_language_code(self):
        with self.assertRaises(InvalidLanguageCodeException) as e:
            mathparse.parse('one plus one', language='123')

        self.assertEqual(
            str(e.exception),
            '123 is not an available language code'
        )

    def test_parsing_with_unsupported_operator(self):
        """
        NOTE: The French language currently is missing support for
        unary_operators. This test will start failing when those are
        added to the language support.
        """
        with self.assertRaises(mathparse.PostfixTokenEvaluationException) as e:
            mathparse.parse(
                # Three times the square root of 4
                'trois fois la racine carrée de 4',
                language='FRE',
                stopwords={'la', 'de'}
            )

        self.assertEqual(
            str(e.exception),
            'Unsupported mathematical term: "racine"'
        )
