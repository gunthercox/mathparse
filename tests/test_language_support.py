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
        Simulate parsing a string with an unsupported operator in a supported
        language. Eg. using "invalid" to represent an unsupported unary
        operator in French.
        """
        with self.assertRaises(mathparse.PostfixTokenEvaluationException) as e:
            mathparse.parse(
                # Three times the invalid root of 4
                'trois fois la invalid carrée de 4',
                language='FRE',
                stopwords={'la', 'de'}
            )

        self.assertEqual(
            str(e.exception),
            'Unsupported mathematical term: "invalid"'
        )
