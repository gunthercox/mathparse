"""
Methods for evaluating mathematical equations in strings.
"""
from __future__ import division
from decimal import Decimal
import re


class PostfixTokenEvaluationException(Exception):
    """
    Exception to be raised when a language code is given that
    is not a part of the ISO 639-2 standard.
    """
    pass


def is_int(string):
    """
    Return true if string is an integer.
    """
    try:
        int(string)
        return True
    except ValueError:
        return False


def is_float(string):
    """
    Return true if the string is a float.
    """
    try:
        float(string)
        return True
    except ValueError:
        return False


def is_unary(string):
    """
    Return true if the string is a defined unary mathematical operator function.
    """
    from .mathwords import FUNCTIONS
    return string in FUNCTIONS


def is_binary(string):
    """
    Return true if the string is a defined binary operator.
    """
    from .mathwords import BINARY_OPERATORS
    return string in BINARY_OPERATORS

def is_word(word, language):
    """
    Return true if the word is a math word for the specified language.
    """
    from .mathwords import words_for_language

    words = words_for_language(language)

    return word in words

def replace_word_tokens(string, language):
    """
    Given a string and an ISO 639-2 language code,
    return the string with the words replaced with
    an operational equivalent.
    """
    from .mathwords import word_groups_for_language

    words = word_groups_for_language(language)

    # Replace operator words with numeric operators
    operators = words['binary_operators'].copy()
    operators.update(words['unary_operators'])
    for operator in operators:
        if operator in string:
            string = string.replace(operator, operators[operator])

    # Replace number words with numeric values
    numbers = words['numbers']
    for number in numbers:
        if number in string:
            string = string.replace(number, str(numbers[number]))

    # Replace scaling multipliers with numeric values
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
    precedence = {
        '/': 4,
        '*': 4,
        '+': 3,
        '-': 3,
        '^': 2,
        '(': 1
    }

    postfix = []
    opstack = []

    for token in tokens:
        if is_int(token):
            postfix.append(int(token))
        elif is_float(token):
            postfix.append(float(token))
        elif is_unary(token):
            opstack.append(token)
        elif token == '(':
            opstack.append(token)
        elif token == ')':
            top_token = opstack.pop()
            while top_token != '(':
                postfix.append(top_token)
                top_token = opstack.pop()
        else:
            while (opstack != []) and (precedence[opstack[-1]] >= precedence[token]):
                postfix.append(opstack.pop())
            opstack.append(token)

    while opstack != []:
        postfix.append(opstack.pop())

    return postfix


def evaluate_postfix(tokens):
    """
    Given a list of evaluatable tokens in postfix format,
    calculate a solution.
    """
    from .mathwords import FUNCTIONS
    stack = []

    for token in tokens:
        total = None

        if is_int(token) or is_float(token):
            stack.append(token)
        elif is_unary(token):
            a = stack.pop()
            total = FUNCTIONS[token](a)
        elif len(stack):
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                total = a + b
            elif token == '-':
                total = a - b
            elif token == '*':
                total = a * b
            elif token == '^':
                total = a ** b
            elif token == '/':
                total = Decimal(str(a)) / Decimal(str(b))
            else:
                raise PostfixTokenEvaluationException('Unknown token {}'.format(token))

        if total is not None:
            stack.append(total)

    # If the stack is empty the tokens could not be evaluated
    if not stack:
        raise PostfixTokenEvaluationException('The postfix expression resulted in an empty stack')

    return stack.pop()


def tokenize(string, language=None, escape='___'):
    """
    Given a string, return a list of math symbol tokens
    """
    from .mathwords import words_for_language

    # Set all words to lowercase
    string = string.lower()

    # Ignore punctuation
    if not string[-1].isalnum():
        character = string[-1]
        string = string[:-1] + ' ' + character

    # Parenthesis must have space around them to be tokenized properly
    string = string.replace('(', ' ( ')
    string = string.replace(')', ' ) ')

    if language:
        words = words_for_language(language)

        for phrase in words:
            escaped_phrase = phrase.replace(' ', escape)
            string = string.replace(phrase, escaped_phrase)

    tokens = string.split()

    for index, token in enumerate(tokens):
        tokens[index] = token.replace(escape, ' ')

    return tokens


def parse(string, language=None):
    """
    Return a solution to the equation in the input string.
    """
    if language:
        string = replace_word_tokens(string, language)

    tokens = tokenize(string)
    postfix = to_postfix(tokens)

    return evaluate_postfix(postfix)


def extract_expression(dirty_string, language):
    """
    Give a string such as: "What is 4 + 4?"
    Return the string "4 + 4"
    """
    tokens = tokenize(dirty_string, language)

    start_index = 0
    end_index = len(tokens)

    for part in tokens:
        if is_int(part) or is_float(part) or is_unary(part) or is_binary(part) or is_word(part, language):
            break
        else:
            start_index += 1

    for part in reversed(tokens):
        if is_int(part) or is_float(part) or is_unary(part) or is_binary(part) or is_word(part, language):
            break
        else:
            end_index -= 1

    return ' '.join(tokens[start_index:end_index])
