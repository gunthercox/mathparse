"""
Methods for evaluating mathematical equations in strings.
"""
import re


def is_int(string):
    try: 
        int(string)
        return True
    except ValueError:
        return False


def replace_word_tokens(string, language):
    """
    Given a string and an ISO 639-2 language code,
    return the string with the words replaced with
    an operational equivalent.
    """
    from .mathwords import words_for_language

    words = words_for_language(language)

    # Replace operator words with numberic operators
    operators = words['operators']
    for operator in operators:
        if operator in string:
            string = string.replace(operator, operators[operator])

    # Replace number words with numeric values
    numbers = words['numbers']
    for number in numbers:
        if number in string:
            string = string.replace(number, str(numbers[number]))

    # Replace scaling multipliers with numberic values
    scales = words['scales']
    for scale in scales:
        if scale in string:
            for match in re.finditer(scale, string):
                index = match.start() - 1
                while is_int(string[index]) and index >= 0:
                    index -= 1
                index -= 1

                string = string[:index] + '(' + string[index:]

                string = string.replace(scale, '* ' + str(scales[scale]) + ')')

    return string


def to_postfix(tokens):
    """
    Convert a list of evaluatable tokens to postfix format.
    """
    stack = []

    return stack


def evaluate_postfix(tokens):
    """
    Given a list of evaluatable tokens in postfix format,
    calculate a solution.
    """

    return 0


def parse(string, language=None):
    """
    Return a solution to the equation in the input string.
    """

    if language:
        string = replace_word_tokens(string, language)

    tokens = to_postfix(string.split())

    return evaluate_postfix(tokens)
