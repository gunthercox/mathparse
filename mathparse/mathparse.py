"""
Methods for evaluating mathematical equations in strings.
"""
from decimal import Decimal
from typing import Union
from . import mathwords
import re


class PostfixTokenEvaluationException(Exception):
    """
    Exception to be raised when a language code is given that
    is not a part of the ISO 639-2 standard.
    """
    pass


def is_int(string: str) -> bool:
    """
    Return true if string is an integer.
    """
    try:
        int(string)
        return True
    except ValueError:
        return False


def is_float(string: str) -> bool:
    """
    Return true if the string is a float.
    """
    try:
        float(string)
        return '.' in string
    except ValueError:
        return False


def is_constant(string: str) -> bool:
    """
    Return true if the string is a mathematical constant.
    """
    return mathwords.CONSTANTS.get(string, False)


def is_unary(string: str) -> bool:
    """
    Return true if the string is a defined unary mathematical
    operator function.
    """
    return string in mathwords.UNARY_FUNCTIONS


def is_binary(string: str) -> bool:
    """
    Return true if the string is a defined binary operator.
    """
    return string in mathwords.BINARY_OPERATORS


def is_symbol(string: str) -> bool:
    """
    Return true if the string is a mathematical symbol.
    """
    return (
        is_int(string) or is_float(string) or
        is_constant(string) or is_unary(string) or
        is_binary(string) or
        (string == '(') or (string == ')')
    )


def is_word(word: str, language: str) -> bool:
    """
    Return true if the word is a math word for the specified language.
    """
    words = mathwords.words_for_language(language)

    return word in words


def find_word_groups(string: str, words: list) -> list:
    """
    Find matches for words in the format "3 thousand 6 hundred 2".
    The words parameter should be the list of words to check for
    such as "hundred".
    """
    scale_pattern = '|'.join(words)
    # For example:
    # (?:(?:\d+)\s+(?:hundred|thousand)*\s*)+(?:\d+|hundred|thousand)+
    regex = re.compile(
        r'(?:(?:\d+)\s+(?:' +
        scale_pattern +
        r')*\s*)+(?:\d+|' +
        scale_pattern + r')+'
    )
    result = regex.findall(string)
    return result


def replace_word_tokens(string: str, language: str) -> str:
    """
    Replace word-based mathematical terms with their symbolic equivalents.

    Given a string and an ISO 639-2 language code,
    return the string with the words replaced with
    an operational equivalent.
    """
    words = mathwords.word_groups_for_language(language)

    # Replace binary operator words with numeric operators
    binary_operators = words['binary_operators']
    for operator in frozenset(binary_operators.keys()):
        if operator in string:
            string = string.replace(operator, binary_operators[operator])

    # Handle prefix unary operators (like "square root of")
    if 'prefix_unary_operators' in words:
        prefix_unary_operators = words['prefix_unary_operators']
        for operator in frozenset(prefix_unary_operators.keys()):
            if operator in string:
                string = string.replace(
                    operator, prefix_unary_operators[operator]
                )

    # Handle postfix unary operators (like "squared", "cubed")
    if 'postfix_unary_operators' in words:
        postfix_unary_operators = words['postfix_unary_operators']
        for operator in frozenset(postfix_unary_operators.keys()):
            if operator in string:
                # Captures the number/operand before the unary operator
                pattern = r'(\w+)\s+' + re.escape(operator)
                replacement = r'(\1 ' + postfix_unary_operators[operator] + ')'
                string = re.sub(pattern, replacement, string)

    # Handle compound numbers (e.g., "twenty one" -> "(20 + 1)", "fifty four" -> "(50 + 4)")
    numbers = words['numbers']

    # Create regex patterns for compound numbers
    # Pattern matches: (tens_word) (units_word) where tens_word is 20,30,40,...,90 and units_word is 1-9
    tens_words = {word: value for word, value in numbers.items() if value in [20, 30, 40, 50, 60, 70, 80, 90]}
    units_words = {word: value for word, value in numbers.items() if value in [1, 2, 3, 4, 5, 6, 7, 8, 9]}

    # Replace compound numbers first (before individual number replacement)
    for tens_word, tens_value in tens_words.items():
        for units_word, units_value in units_words.items():
            compound_pattern = tens_word + r'\s+' + units_word
            compound_replacement = f'({tens_value} + {units_value})'
            if re.search(compound_pattern, string):
                string = re.sub(compound_pattern, compound_replacement, string)

    # Replace number words with numeric values
    for number in frozenset(numbers.keys()):
        if number in string:
            string = string.replace(number, str(numbers[number]))

    # Remove words that are not registered mathematical terms
    # (typically stopwords)
    all_math_words = mathwords.words_for_language(language)
    word_list = string.split()
    symbol_characters = frozenset('0123456789+-*/^().')
    filtered_words = []
    for word in word_list:
        # Keep the word if it is a mathematical symbol, a registered math word.
        # A word is considered a mathematical symbol if it contains digits,
        # operators, or parentheses.
        contains_math_chars = any(c in word for c in symbol_characters)
        if (is_symbol(word) or contains_math_chars or word in all_math_words):
            filtered_words.append(word)

    # Replace scaling multipliers with numeric values
    string = ' '.join(filtered_words)
    scales = words['scales']
    end_index_characters = mathwords.BINARY_OPERATORS
    end_index_characters.add('(')

    word_matches = find_word_groups(string, frozenset(scales.keys()))

    for match in word_matches:
        string = string.replace(match, '(' + match + ')')

    for scale in frozenset(scales.keys()):
        for _ in range(0, string.count(scale)):
            start_index = string.find(scale) - 1
            end_index = len(string)

            while is_int(string[start_index - 1]) and start_index > 0:
                start_index -= 1

            end_index = string.find(' ', start_index) + 1
            end_index = string.find(' ', end_index) + 1

            add = ' + '
            if string[end_index] in end_index_characters:
                add = ''

            string = string[:start_index] + '(' + string[start_index:]
            string = string.replace(
                scale, '* ' + str(scales[scale]) + ')' + add,
                1
            )

    string = string.replace(') (', ') + (')

    return string


def to_postfix(tokens: list) -> list:
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

    # Unary functions have a higher precedence than binary operators
    unary_precedence = max(precedence.values()) + 1

    postfix = []
    opstack = []

    for token in tokens:
        if is_int(token):
            postfix.append(int(token))
        elif is_float(token):
            postfix.append(float(token))
        elif token in mathwords.CONSTANTS:
            postfix.append(mathwords.CONSTANTS[token])
        elif is_unary(token):
            opstack.append(token)
        elif token == '(':
            opstack.append(token)
        elif token == ')':
            top_token = opstack.pop()
            while top_token != '(':
                postfix.append(top_token)
                top_token = opstack.pop()
        elif is_binary(token):
            # For binary operators, pop operators with higher or
            # equal precedence
            while (opstack != []) and (
                (
                    opstack[-1] in precedence and token in precedence and (
                        precedence[opstack[-1]] >= precedence[token]
                    )
                ) or
                (
                    is_unary(
                        opstack[-1]
                    ) and unary_precedence >= precedence[token]
                )
            ):
                postfix.append(opstack.pop())
            opstack.append(token)
        else:
            # Skip tokens that are not mathematical symbols (stopwords, etc.)
            continue

    while opstack != []:
        postfix.append(opstack.pop())

    return postfix


def evaluate_postfix(tokens: list) -> Union[int, float, str, Decimal]:
    """
    Given a list of evaluatable tokens in postfix format,
    calculate a solution.
    """
    stack = []

    for token in tokens:
        total = None

        if is_int(token) or is_float(token) or is_constant(token):
            stack.append(token)
        elif is_unary(token):
            a = stack.pop()
            total = mathwords.UNARY_FUNCTIONS[token](a)
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
                if Decimal(str(b)) == 0:
                    total = 'undefined'
                else:
                    total = Decimal(str(a)) / Decimal(str(b))
            else:
                raise PostfixTokenEvaluationException(
                    'Unknown token "{}"'.format(token)
                )

        if total is not None:
            stack.append(total)

    # If the stack is empty the tokens could not be evaluated
    if not stack:
        raise PostfixTokenEvaluationException(
            'The postfix expression resulted in an empty stack'
        )

    return stack.pop()


def tokenize(string: str, language: str = None, escape: str = '___') -> list:
    """
    Convert a string into a list of mathematical tokens for processing.

    Args:
        string (str): The input string containing a mathematical expression.

        language (str, optional): ISO 639-2 language code for word-based
            parsing. If None, only numeric expressions
            are supported.

        escape (str, optional): A string used to temporarily replace spaces
            in multi-word phrases during tokenization.
            Default is '___'.

    Returns:
        list: A list of tokens extracted from the input string.
    """
    # Set all words to lowercase
    string = string.lower()

    # Ignore punctuation
    if len(string) and not string[-1].isalnum():
        character = string[-1]
        string = string[:-1] + ' ' + character

    # Parenthesis must have space around them to be tokenized properly
    string = string.replace('(', ' ( ')
    string = string.replace(')', ' ) ')

    if language:
        words = mathwords.words_for_language(language)

        for phrase in words:
            escaped_phrase = phrase.replace(' ', escape)
            string = string.replace(phrase, escaped_phrase)

    tokens = string.split()

    for index, token in enumerate(tokens):
        tokens[index] = token.replace(escape, ' ')

    return tokens


def parse(
    string: str, language: str = None
) -> Union[int, float, str, Decimal]:
    """
    Parse and evaluate a mathematical expression from a string.

    This is the main entry point for mathparse. It can handle both numeric
    expressions (like "2 + 3 * 4") and word-based expressions in various
    languages (like "five plus three" in English).

    Args:
        string (str): The mathematical expression to parse and evaluate.
                     Can contain numbers, operators, parentheses, constants,
                     and functions. For word-based parsing, must use terms
                     from the specified language.
        language (str, optional): ISO 639-2 language code for word-based
                                parsing. Supported codes: 'ENG', 'FRE', 'GER',
                                'GRE', 'ITA', 'MAR', 'RUS', 'POR'. If None,
                                only numeric expressions are supported.

    Returns:
        int, float, or str: The result of the mathematical expression.
                           Returns 'undefined' for division by zero.
                           For division operations, returns a Decimal object
                           to maintain precision.

    Raises:
        InvalidLanguageCodeException:
            An unsupported language code was provided.
        PostfixTokenEvaluationException:
            The expression cannot be evaluated.

    Examples:
        >>> parse('2 + 3 * 4')
        14

        >>> parse('five plus three', language='ENG')
        8

        >>> parse('(seven * nine) + 8 - (45 plus two)', language='ENG')
        24

        >>> parse('sqrt 16')
        4.0

        >>> parse('pi * 2')
        6.283386

        >>> parse('10 / 0')
        'undefined'

    Note:
        - Follows standard order of operations (PEMDAS)
        - Supports mathematical constants: pi, e
        - Supports unary functions: sqrt, log
        - Each expression must use terms from a single language
        - Division by zero returns 'undefined' instead of raising an exception
    """
    if language:
        string = replace_word_tokens(string, language)

    tokens = tokenize(string)
    postfix = to_postfix(tokens)

    return evaluate_postfix(postfix)


def extract_expression(dirty_string: str, language: str) -> str:
    """
    Extract a mathematical expression from a sentence containing extra text.

    This function identifies and extracts the mathematical portion from
    natural language sentences like:
    "What is 4 + 4?" or "Calculate five plus three".
    It works by finding the longest sequence of mathematical symbols and words.

    Args:
        dirty_string (str): A sentence or phrase containing a mathematical
                          expression mixed with other text.
        language (str): ISO 639-2 language code to identify mathematical
                       words in the target language.

    Returns:
        str: The extracted mathematical expression as a string.

    Examples:
        >>> extract_expression("What is 5 plus 3?", language='ENG')
        '5 plus 3'

        >>> extract_expression(
                "Please calculate two times seven", language='ENG'
            )
        'two times seven'

        >>> extract_expression(
                "The result of 10 / 2 should be 5", language=None
            )
        '10 / 2'

    Note:
        - The function looks for continuous sequences of mathematical terms
        - Non-mathematical words at the beginning and end are stripped
        - The language parameter is required to identify word-based math terms
    """
    tokens = tokenize(dirty_string, language)

    start_index = 0
    end_index = len(tokens)

    for part in tokens:
        if is_symbol(part) or is_word(part, language):
            break
        else:
            start_index += 1

    for part in reversed(tokens):
        if is_symbol(part) or is_word(part, language):
            break
        else:
            end_index -= 1

    return ' '.join(tokens[start_index:end_index])
