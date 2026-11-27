# AI Agent Instructions for mathparse

## Architecture Overview

mathparse is a **mathematical expression evaluator** that safely parses and evaluates mathematical expressions from strings, supporting both numeric operators and natural language words across multiple languages.

### Core Components

- **`mathparse/mathparse.py`**: Main evaluation engine with three-phase pipeline
- **`mathparse/mathwords.py`**: Language definitions and multilingual mathematical vocabularies
- **`mathparse/__init__.py`**: Simple module entry point

### Key Data Flow

1. **Tokenization** (`tokenize()`) - Convert strings to mathematical tokens
2. **Word Replacement** (`replace_word_tokens()`) - Transform natural language to symbolic math
3. **Postfix Conversion** (`to_postfix()`) - Convert infix to postfix notation for safe evaluation
4. **Evaluation** (`evaluate_postfix()`) - Calculate result without using Python's `eval()`

**CRITICAL**: The postfix (RPN) evaluation system is the architectural foundation. Prefer extending the postfix evaluator over adding complex regex parsing when implementing new features.

## Critical Design Principles

### Security First
- **Never use `eval()`** - This is the project's core security principle
- All mathematical evaluation goes through controlled postfix evaluation
- Division by zero returns `'undefined'` string, never raises exceptions

### Postfix (RPN) Architecture Priority
- **Always prefer postfix evaluation over regex parsing** for new mathematical operations
- The `to_postfix()` and `evaluate_postfix()` functions handle operator precedence correctly
- Add new operators to `BINARY_OPERATORS` or `UNARY_FUNCTIONS` rather than complex regex rules
- Postfix notation eliminates ambiguity and provides consistent evaluation order
- When implementing new features, consider: "Can this be solved by extending the postfix evaluator?"
- **Think creatively about what constitutes an "operator"**: Binary operators don't just perform arithmetic—they can also construct values (e.g., decimal point combines integer and fractional parts)
- If a feature takes two inputs and produces one output, it can likely be modeled as a binary operator
- Before adding preprocessing logic, ask: "Could this be an operator with custom evaluation logic?"

### Multi-language Support
- Language codes follow **ISO 639-2** standard (3-letter codes like 'ENG', 'FRE')
- Each language in `MATH_WORDS` dict has structured sections:
  - `numbers`: word-to-number mappings
  - `binary_operators`: mathematical operations
  - `scales`: multipliers (hundred, thousand, etc.)
  - `prefix_unary_operators`: functions like "square root of"
  - `postfix_unary_operators`: suffixes like "squared"

### Generic Solutions Over Language-Specific
- **Prefer generic, cross-language solutions** over language-specific implementations
- When solving parsing issues, first consider if the solution can work for all languages
- Language-specific code should only be used when truly necessary for linguistic differences
- Examples of preferred approaches:
  - ✅ Extend `UNARY_FUNCTIONS` for new mathematical operations (works for all languages)
  - ✅ Improve operator precedence handling in postfix evaluation (universal benefit)
  - ✅ Enhance compound operator processing by length-based sorting (helps all languages)
  - ❌ Hard-code regex patterns for specific language character sets
  - ❌ Add language-specific preprocessing unless absolutely required
- If language-specific code is necessary, isolate it clearly and document why the generic approach wasn't sufficient

### Use mathwords.py Definitions, Avoid Hard-Coding
- **Always reference `mathwords.py` definitions** instead of hard-coding mathematical tokens
- Use `BINARY_OPERATORS`, `UNARY_FUNCTIONS`, and language dictionaries as the source of truth
- Examples of preferred approaches:
  - ✅ Use `mathwords.BINARY_OPERATORS` to get valid operators: `{'^', '*', '/', '+', '-'}`
  - ✅ Reference `words['binary_operators'].keys()` for language-specific operators
  - ✅ Check `mathwords.UNARY_FUNCTIONS.keys()` for valid unary functions
  - ✅ Use `mathwords.CONSTANTS` for mathematical constants
  - ✅ Create local copies for temporary modifications: `local_ops = mathwords.BINARY_OPERATORS.copy(); local_ops.add('(')`
  - ✅ Use set operations for combining: `mathwords.BINARY_OPERATORS | {'(', ')'}`
  - ❌ Hard-code operator strings like `"+-*/"` or `['+', '-', '*', '/']` in regex patterns
  - ❌ Hard-code function names like `['sqrt', 'log']` instead of using `UNARY_FUNCTIONS`
  - ❌ Duplicate mathematical definitions that already exist in `mathwords.py`
  - ❌ Directly mutate mathwords definitions: `ops = mathwords.BINARY_OPERATORS; ops.add('(')` (creates reference, modifies global state)
- **Key distinction**: Assignment creates a reference, not a copy. Use `.copy()` or set operations for local modifications
- **Benefits**: Ensures consistency, maintains single source of truth, automatically supports new operators when added
- **Pattern**: Import from `mathwords` and use the dictionaries: `from . import mathwords`

## Development Patterns

### Operator Design Philosophy
When adding new functionality, consider modeling it as an operator rather than special preprocessing:

**Example: Decimal Point Implementation**
- **Problem**: Parse "fifty three point four" → 53.4
- **Naive approach**: ❌ Add regex to detect "point" pattern and replace with "53.4" during preprocessing
- **Better approach**: ✅ Treat "point" as a binary operator:
  1. Add `'point': '.'` to language `binary_operators`
  2. Add `'.'` to global `BINARY_OPERATORS`
  3. Define precedence (highest, so it binds before other operations)
  4. Implement evaluation: `a . b = a + (b / 10^digits_in_b)`
- **Benefits**: Generic solution, works with any expression, follows architecture, extensible to all languages

**Questions to ask when designing features:**
- Does this transform two values into one? → Probably a binary operator
- Does this transform one value? → Probably a unary function
- Does this combine multiple similar values? → Might need preprocessing (like compound numbers)

### Testing Structure
Tests are organized by **operation type**, not by language:
- `test_binary_operations.py` - Addition, subtraction, multiplication, division
- `test_unary_operations.py` - Square root, logarithms, powers
- `test_complex_statements.py` - Multi-step expressions with precedence
- `test_language_support.py` - Language-specific edge cases

### Language Implementation Pattern
When adding new languages to `mathwords.py`:
```python
'XXX': {  # ISO 639-2 code
    'binary_operators': {'word': 'symbol'},
    'numbers': {'word': value},
    'scales': {'word': multiplier},
    # Optional sections:
    'prefix_unary_operators': {'phrase': 'function'},
    'postfix_unary_operators': {'suffix': '^ power'}
}
```

### Error Handling Convention
- Use `PostfixTokenEvaluationException` for parsing/evaluation errors
- Use `InvalidLanguageCodeException` for unsupported languages
- Division by zero returns `'undefined'` string (not exception)
- Missing language features raise `PostfixTokenEvaluationException` with clear message

## Key Functions & Usage

### Main Entry Point
```python
mathparse.parse(string, language=None, stopwords=None)
```
- `language`: Required for word-based expressions
- `stopwords`: Set of words to ignore (e.g., `{'the', 'of'}`)

### Token Processing
- `is_int()`, `is_float()`, `is_symbol()` - Type checking utilities
- `replace_word_tokens()` - Handles compound numbers like "twenty one" → "(20 + 1)"
- `extract_expression()` - Extracts math from natural language sentences

### Postfix Evaluation Design
- `to_postfix()` - Converts infix notation to postfix (RPN) using operator precedence
- `evaluate_postfix()` - Safe evaluation without `eval()` using stack-based RPN algorithm
- **Precedence handling**: Higher numbers = tighter binding. Example: decimal (5) > division/multiplication (4) > addition/subtraction (3) > power (2) > parentheses (1)
- **Extension pattern**: Add new operators to precedence dictionary, then implement their evaluation logic
- **Operator flexibility**: Binary operators can perform any two-input, one-output transformation:
  - Arithmetic: `+, -, *, /, ^`
  - Construction: `.` (decimal point combines 53 and 4 into 53.4)
  - Future examples: `:` (ratio), `//` (integer division), `%` (modulo)

## Build & Test Commands

```bash
# Install with test dependencies
python -m pip install .[test]

# Run all tests
python -m unittest discover -s tests

# Lint code
flake8 . --show-source --statistics

# Build documentation
sphinx-build -nW -b html ./docs/ ./build/
```

## Code Quality Standards

### Linting with flake8
- **Always run flake8** before committing code changes
- All code must pass flake8 with **zero errors and warnings**
- Configuration follows PEP 8 style guide with 79 character line limit

### Common flake8 Issues to Avoid
- **E501**: Line too long (> 79 characters)
  - Break long lines at logical points
  - Use parentheses for implicit line continuation
  - Keep comments within the 79 character limit
- **W293**: Blank lines containing whitespace
  - Remove all trailing whitespace from blank lines
  - Use editor settings to strip trailing whitespace on save
- **E302/E305**: Expected blank lines
  - 2 blank lines before top-level functions/classes
  - 1 blank line between methods in a class
- **F401**: Imported but unused
  - Remove unused imports
- **E711/E712**: Comparison to None/True/False
  - Use `is None` / `is not None`
  - Use `if variable:` instead of `if variable is True:`

### Code Style Guidelines
- **Line length**: Maximum 79 characters
- **Indentation**: 4 spaces (no tabs)
- **Blank lines**: 
  - 2 blank lines around top-level functions and classes
  - 1 blank line between methods
  - Use sparingly within functions for logical grouping
- **Comments**: 
  - Inline comments: 2 spaces after code, start with `#` and space
  - Block comments: Start with `#` and space, align with code
  - Keep within 79 character limit
- **Docstrings**: 
  - Triple double-quotes for all public modules, functions, classes, methods
  - Always use multi-line format with opening `"""` and closing `"""` on separate lines
  - Example format:
    ```python
    def my_function():
        """
        Brief description of the function.

        More detailed explanation if needed.
        """
    ```
  - Never use single-line format like `"""Text"""`
  - Follow Google or NumPy docstring format
  - Include Args, Returns, Raises sections where applicable
  - Ensure closing `"""` is on its own line

### Pre-commit Checklist
1. Run `flake8 . --show-source --statistics` → Must show 0 errors
2. Run `python -m unittest discover -s tests` → All tests must pass
3. Check git diff to ensure only intended changes are included
4. Verify docstrings are updated for any API changes

### When Fixing Linting Issues
- Fix whitespace issues first (W293, trailing spaces)
- Then fix line length issues (E501) by refactoring, not just adding line breaks
- Ensure fixes don't change functionality
- Run tests after each fix to prevent regressions
- Commit linting fixes separately from feature/bug fix commits when possible

## Constants & Limitations

- **Mathematical constants**: `pi` (3.141693), `e` (2.718281) in `CONSTANTS`
- **Unary functions**: `sqrt`, `log` (base 10) in `UNARY_FUNCTIONS`
- **Python version**: Requires Python 3.11-3.14
- **Zero dependencies**: Pure Python implementation

## Language Extension Guidelines

- Test each new language with compound numbers, scales, and all operator types
- Include both prefix ("square root of") and postfix ("squared") unary operators where applicable
- Handle hyphenated compound numbers (e.g., "twenty-one")
- Verify precedence rules work correctly with word operators