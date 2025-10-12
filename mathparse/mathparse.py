"""
Methods for evaluating mathematical equations in strings.
"""
from decimal import Decimal
from typing import Union
from . import mathwords
import re


class PostfixTokenEvaluationException(Exception):
    """
    Exception to be raised when an expression cannot be evaluated.
    """
    pass


def is_int(string: str) -> bool:
    """
    Return true if string is an integer.
    """
    # Allow leading minus sign
    if string[0] == '-':
        # Must have at least one digit after the minus
        return len(string) > 1 and string[1:].isdigit()
    else:
        # Must be all digits
        return string.isdigit()


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


def to_number(val) -> Union[int, float, str, Decimal]:
    """
    Convert a string to an int or float if possible.
    """
    # If already a number (int, float, Decimal), return as-is
    if isinstance(val, (int, float, Decimal)):
        return val

    # Check if it's a constant and convert
    if is_constant(val):
        return mathwords.CONSTANTS[val]

    # Otherwise, try to convert string to number
    if is_int(val):
        return int(val)
    elif is_float(val):
        return float(val)

    return val


def create_unicode_word_boundary_pattern(word: str) -> str:
    """
    Create a regex pattern with Unicode-aware word boundaries.

    Standard regex \\b word boundaries don't work with non-ASCII characters
    (e.g., Devanagari, Arabic, Hebrew, Chinese, Thai, etc.). This function
    creates a pattern that works across all Unicode scripts.

    Args:
        word (str): The word to create a boundary pattern for

    Returns:
        str: A regex pattern string with proper Unicode boundaries

    Examples:
        >>> create_unicode_word_boundary_pattern("two")
        '(?<![\\w])two(?![\\w])'
        >>> create_unicode_word_boundary_pattern("दो")  # Hindi "two"
        '(?:^|(?<=[\\s+\\-*/^()]))दो(?:$|(?=[\\s+\\-*/^()]))'
    """
    # Check if word contains only ASCII alphanumeric characters
    if word.isascii() and word.replace('-', '').replace("'", '').isalnum():
        # For ASCII words, use standard word boundaries
        return r'\b' + re.escape(word) + r'\b'
    else:
        # For non-ASCII (Unicode) words, use space/operator boundaries
        # This pattern matches the word when it's:
        # - At the start of string OR preceded by whitespace/operator
        # - At the end of string OR followed by whitespace/operator
        escaped_word = re.escape(word)
        # Boundary characters: whitespace, operators, parentheses
        boundary = r'[\s+\-*/^()]'
        return f'(?:^|(?<={boundary})){escaped_word}(?:$|(?={boundary}))'


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


def replace_word_tokens_simplified_chinese(
    string, stopwords: set[str] = None
) -> str:
    """
    simplified Chinese version:
    Given a string and an ISO 639-2 language code,
    return the string with the words replaced with
    an operational equivalent.
    """
    words = mathwords.word_groups_for_language('CHI')

    # Handle special Chinese power construction patterns FIRST
    # In Chinese, '的...次方' forms a power construction where:
    # - '的' acts as a possessive/linking word (provides the ^ operator)
    # - '次方' is a suffix meaning "power" (should be removed, not replaced)
    # - '次幂' is similar to '次方'
    # Example: 二的四次方 = 2's 4th power = 2 ^ 4
    # We need to remove '次方' and '次幂' BEFORE they get replaced as operators
    string = string.replace('次方', ' ')
    string = string.replace('次幂', ' ')

    # Collect all operators (binary, prefix unary, postfix unary)
    # and process them by length (longest first) to handle cases where
    # a shorter operator is a substring of a longer one
    # Example: '平方' (squared) vs '平方根' (square root)
    all_operators = {}

    # Add binary operators
    all_operators.update(words['binary_operators'])

    # Add prefix unary operators
    all_operators.update(words['prefix_unary_operators'])

    # Add postfix unary operators
    if 'postfix_unary_operators' in words:
        all_operators.update(words['postfix_unary_operators'])

    # Sort all operators by length (longest first)
    sorted_operators = sorted(all_operators.keys(), key=len, reverse=True)

    for operator in sorted_operators:
        if operator in string:
            # 中文没有分隔符，后面需要靠分隔符分割式子，每次识别一个符号都将其分开来
            string = string.replace(
                operator, ' ' + all_operators[operator] + ' '
            )

    # chinese_scales用list的原因是为了保持从大到小的顺序，亿、万、千...
    # Sort scales by their numeric value (largest first) to ensure correct
    # parsing. For example, '千' (1000) should be found before '百' (100)
    digits = set(words['numbers'].keys())
    scales = sorted(
        words['scales'].keys(), key=lambda x: words['scales'][x], reverse=True
    )
    digits_scales = words['numbers'].copy()
    digits_scales.update(words['scales'])

    # 九千八百万九千八百——> 98009800
    def chinese_string_to_num(str):
        if str == '':
            return 0

        if str in digits:
            return digits_scales[str]

        digits_scales.update(words['scales'])

        for scale in scales:
            index = str.find(scale)
            if index >= 0:
                t1 = chinese_string_to_num(str[:index])
                t2 = digits_scales[scale]
                t3 = chinese_string_to_num(str[index + 1:])
                return t1 * t2 + t3
        else:
            return digits_scales[str]

    # 扫描看有没有汉字数字，有转化为阿拉伯数字
    index = 0
    start = end = 0
    while True:
        char = string[index]

        if char in digits_scales:
            end += 1
            index += 1
        else:
            if start < end:
                num = str(chinese_string_to_num(string[start:end]))
                # 需要加多一个分隔符
                num_str = str(num) + ' '
                string = string[:start] + num_str + string[end:]
                index = start + len(num_str)
                start = end = index
            else:
                index += 1
                start = end = index

        if index >= len(string):
            if start < end:
                num = str(chinese_string_to_num(string[start:end]))
                num_str = str(num) + ' '
                string = string[:start] + num_str + string[end:]

            break

    return string


def replace_word_tokens(
    string: str, language: str, stopwords: set[str] = None
) -> str:
    """
    Replace word-based mathematical terms with their symbolic equivalents.

    Given a string and an ISO 639-2 language code,
    return the string with the words replaced with
    an operational equivalent.

    Args:
        string (str): The input string containing a mathematical expression
                      with words.

        language (str): ISO 639-2 language code for word-based parsing.

        stopwords (set[str], optional): A set of words to ignore during
                                       parsing. This can be used to filter out
                                       non-mathematical words in expressions.

    Returns:
        str: The input string with word-based mathematical terms replaced
             with their symbolic equivalents.
    """
    words = mathwords.word_groups_for_language(language)

    # Process operators by length (longest first) to handle compound operators
    binary_operators = words['binary_operators']
    sorted_operators = sorted(binary_operators.keys(), key=len, reverse=True)
    for operator in sorted_operators:
        if operator in string:
            string = string.replace(operator, binary_operators[operator])

    # Handle prefix unary operators (like "square root of")
    if 'prefix_unary_operators' in words:
        prefix_unary_operators = words['prefix_unary_operators']
        # Sort by length to handle compound operators where a shorter token
        # is a substring of a longer token
        sorted_prefix_operators = sorted(
            prefix_unary_operators.keys(), key=len, reverse=True
        )
        for operator in sorted_prefix_operators:
            if operator in string:
                string = string.replace(
                    operator, prefix_unary_operators[operator]
                )

    # Handle postfix unary operators (like "squared", "cubed")
    if 'postfix_unary_operators' in words:
        postfix_unary_operators = words['postfix_unary_operators']
        # Sort by length to handle compound operators where a shorter token
        # is a substring of a longer token
        sorted_postfix_operators = sorted(
            postfix_unary_operators.keys(), key=len, reverse=True
        )
        for operator in sorted_postfix_operators:
            if operator in string:
                # Captures the number/operand before the unary operator
                pattern = r'(\w+)\s+' + re.escape(operator)
                replacement = r'(\1 ' + postfix_unary_operators[operator] + ')'
                string = re.sub(pattern, replacement, string)

    # Handle compound numbers:
    # (e.g., "twenty one" -> "(20 + 1)", "fifty four" -> "(50 + 4)")
    numbers = words['numbers']

    # Create regex patterns for compound numbers
    # Pattern matches: (tens_word) (units_word) where tens_word is
    # 20,30,40,...,90 and units_word is 1-9
    tens_words = {word: value for word, value in numbers.items() if value in [
        20, 30, 40, 50, 60, 70, 80, 90
    ]}
    units_words = {word: value for word, value in numbers.items() if value in [
        1, 2, 3, 4, 5, 6, 7, 8, 9
    ]}

    # Preprocess hyphenated compound numbers
    # (e.g., "fifty-four" -> "fifty four")
    for tens_word in tens_words.keys():
        for units_word in units_words.keys():
            hyphenated_pattern = tens_word + r'-' + units_word
            space_separated = tens_word + ' ' + units_word
            if re.search(hyphenated_pattern, string):
                string = re.sub(hyphenated_pattern, space_separated, string)

    # Replace compound numbers first (before individual number replacement)
    for tens_word, tens_value in tens_words.items():
        for units_word, units_value in units_words.items():
            compound_pattern = tens_word + r'\s+' + units_word
            compound_replacement = f'({tens_value} + {units_value})'
            if re.search(compound_pattern, string):
                string = re.sub(compound_pattern, compound_replacement, string)

    # Replace number words with numeric values
    for number in frozenset(numbers.keys()):
        # Use Unicode-aware word boundaries to prevent partial matches
        # (e.g., "nine" in "nineteen") and support non-ASCII scripts
        # (e.g., Devanagari, Arabic, Hebrew, Chinese, etc.)
        pattern = create_unicode_word_boundary_pattern(number)
        if re.search(pattern, string):
            string = re.sub(pattern, str(numbers[number]), string)

    # Remove words specified to be ignored
    if stopwords:
        filtered_words = []

        for word in string.split():
            if word not in stopwords:
                filtered_words.append(word)
        string = ' '.join(filtered_words)

    # Replace scaling multipliers with numeric values
    scales = words['scales']
    end_index_characters = mathwords.BINARY_OPERATORS | {'('}

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

    # Remove extra parentheses around all scale expressions to simplify output
    # Convert ((number * scale)) to (number * scale) for all scales
    string = re.sub(r'\(\((\d+\s*\*\s*\d+)\)\)', r'(\1)', string)

    return string


def preprocess_unary_operators(tokens: list) -> list:
    """
    Preprocess tokens to convert unary minus to the 'neg' function.

    A minus sign is considered unary (negative) if it appears:
    * At the beginning of the expression
    * After an opening parenthesis '('
    * After a binary operator `(+, -, *, /, ^)`
    * After a unary function `(sqrt, log, neg)`
    """
    if not tokens:
        return tokens

    processed_tokens = []

    # A following minus sign should be treated as unary (negative)
    unary_contexts = mathwords.BINARY_OPERATORS | {'('}

    for i, token in enumerate(tokens):
        if token == '-':
            # Check if this minus should be treated as unary
            is_unary_minus = False

            if i == 0:
                # The first token is unary minus
                is_unary_minus = True
            elif i > 0:
                prev_token = tokens[i - 1]
                # A unary minus after opening parenthesis, binary operators,
                # or unary functions
                if prev_token in unary_contexts or is_unary(prev_token):
                    is_unary_minus = True

            if is_unary_minus:
                # Convert the unary minus to 'neg' function
                processed_tokens.append('neg')
            else:
                # Keep as binary minus
                processed_tokens.append(token)
        else:
            processed_tokens.append(token)

    return processed_tokens


def to_postfix(tokens: list) -> list:
    """
    Convert a list of evaluatable tokens to postfix format.
    """
    precedence = {
        '.': 5,
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
            postfix.append(token)
        elif is_float(token):
            postfix.append(token)
        elif token in mathwords.CONSTANTS:
            postfix.append(token)
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
            # Raise exception for unsupported mathematical terms
            raise PostfixTokenEvaluationException(
                'Unsupported mathematical term: "{}"'.format(token)
            )

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
            # Convert token (string) to number for unary function evaluation
            a = to_number(a)
            total = mathwords.UNARY_FUNCTIONS[token](a)
        elif len(stack) == 1:
            raise PostfixTokenEvaluationException(
                'Insufficient values in expression for operator "{}"'.format(
                    token
                )
            )
        elif len(stack) > 1:
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                total = to_number(a) + to_number(b)
            elif token == '-':
                total = to_number(a) - to_number(b)
            elif token == '*':
                total = to_number(a) * to_number(b)
            elif token == '^':
                total = to_number(a) ** to_number(b)
            elif token == '/':
                if Decimal(str(b)) == 0:
                    total = 'undefined'
                else:
                    total = Decimal(str(a)) / Decimal(str(b))
            elif token == '.':
                # Treat decimal points as a binary operator that combines the
                # integer and fractional part of two numbers
                # Example: 53 . 25 = 53.25, -3 . 5 = -3.5

                # Convert b to number
                numeric_b = to_number(b)

                if numeric_b == 0:
                    # Convert a to number
                    numeric_a = to_number(a)
                    total = Decimal(numeric_a)
                else:
                    # Check if 'a' has a negative sign (handles -0 case)
                    is_negative = str(a).startswith('-')

                    # Convert a to number for calculation
                    numeric_a = to_number(a)

                    # Count the digits in the original string b to preserve
                    # leading zeros (e.g., "01" has 2 digits, not 1)
                    digits = len(str(b))
                    divisor = 10 ** digits
                    fractional_part = numeric_b / divisor

                    # Handle negatives: -3 . 5 = -3.5, not -2.5
                    # Also -0 . 5 = -0.5 (check string since -0 == 0)
                    if is_negative:
                        total = numeric_a - fractional_part
                    else:
                        total = numeric_a + fractional_part
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

    result = stack.pop()

    # Convert final result from string to number if needed
    if isinstance(result, str):
        if is_int(result):
            result = int(result)
        elif is_float(result):
            result = float(result)

    return result


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

    # If language is specified, normalize compound operators by removing
    # spaces between their characters. This handles cases like '乘 以'
    # which should be treated as the single compound operator '乘以'.
    # Process by length (longest first) to avoid partial matches.
    if language:
        words = mathwords.words_for_language(language)

        # Sort all phrases by length (longest first) to handle cases where
        # a shorter phrase is a substring of a longer one
        phrases_by_length = sorted(words, key=len, reverse=True)

        for phrase in phrases_by_length:
            # For multi-character phrases, create a spaced version
            # and replace it with the non-spaced version
            if len(phrase) > 1:
                # Create pattern with optional spaces between each character
                # For example, '乘以' could appear as '乘 以' or '乘  以'
                spaced_phrase = ' '.join(phrase)
                # Replace spaced version with non-spaced version
                string = string.replace(spaced_phrase, phrase)

    # Binary operators must have space around them to be tokenized properly
    # Special handling for minus sign: preserve leading negatives
    for operator in mathwords.BINARY_OPERATORS:
        if operator == '-':
            # For minus sign, use a pattern that only spaces it when it's
            # clearly a binary operator (after digits or closing parenthesis).
            # This preserves leading negatives like "-3" and distinguishes
            # between:
            # - "What is -3 + 3" --> "-3 + 3" (minus is part of number)
            # - "5 - 3" --> "5 - 3" (minus is binary operator, needs spacing)
            # - "math - 4" --> "- 4" (minus after letters is not a binary
            #   operator)
            # Only add spaces around minus when preceded by a digit or closing
            # parenthesis
            string = re.sub(r'([\d)])\s*-\s*', r'\1 - ', string)
        else:
            string = string.replace(operator, f' {operator} ')

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
    string: str, language: str = None, stopwords: set[str] = None
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
        stopwords (set[str], optional): A set of words to ignore during
                                       parsing. This can be used to filter out
                                       non-mathematical words in expressions.

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
        if language == 'CHI':
            string = replace_word_tokens_simplified_chinese(
                string, stopwords
            )
        else:
            string = replace_word_tokens(string, language, stopwords)

    tokens = tokenize(string, language)
    tokens = preprocess_unary_operators(tokens)
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

    # Find the start of the mathematical expression
    # Skip over non-mathematical tokens AND isolated binary operators
    for i, part in enumerate(tokens):
        if is_symbol(part) or is_word(part, language):
            # A potential start was found, so check if it's a standalone binary
            # operator. Binary operators (except '(') are only valid at the
            # start if they are unary (such as a leading minus for a negative
            # number)
            if part in mathwords.BINARY_OPERATORS and part != '(':
                # For a binary operator to be the start of an expression, it
                # must be:
                # 1. At the very beginning (position 0) - could be unary minus
                # 2. OR all previous tokens were non-mathematical - also could
                #    be unary
                # If there were non-math tokens before it, it's likely a
                # separator

                # Check if all previous tokens are non-mathematical
                all_prev_non_math = True
                for j in range(i):
                    if is_symbol(tokens[j]) or is_word(tokens[j], language):
                        all_prev_non_math = False
                        break

                # Only include this operator if at start OR all previous
                # non-math AND followed by a mathematical token
                if all_prev_non_math and i + 1 < len(tokens):
                    next_token = tokens[i + 1]
                    if (
                        is_int(next_token) or is_float(next_token) or
                        is_constant(next_token) or is_unary(next_token) or
                        next_token == '(' or is_word(next_token, language)
                    ):
                        start_index = i
                        break
            else:
                # Start indexes can be an opening parenthesis, or a non-binary
                # operator
                start_index = i
                break

    for part in reversed(tokens):
        if is_symbol(part) or is_word(part, language):
            break
        else:
            end_index -= 1

    result = ' '.join(tokens[start_index:end_index])

    # Remove spaces around decimal points for cleaner output
    # Replace " . " with "." to convert "-100 . 5" to "-100.5"
    result = result.replace(' . ', '.')

    return result
