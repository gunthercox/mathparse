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


def parse(string, language=None):
    """
    Return a solution to the equation in the input string.
    """
    if language:
        string = replace_word_tokens(string, language)

    # Parenthesis must have space around them to be tokenized properly
    string = string.replace('(', ' ( ')

    tokens = to_postfix(string.split())

    return evaluate_postfix(tokens)
