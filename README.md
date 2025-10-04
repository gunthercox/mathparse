# mathparse

The `mathparse` library is a Python module designed to evaluate mathematical equations contained in strings.

Here are a few examples:

```python
from mathparse import mathparse

mathparse.parse('50 * (85 / 100)')
>>> 42.5

mathparse.parse('one hundred times fifty four', language='ENG')
>>> 5400

mathparse.parse('(seven * nine) + 8 - (45 plus two)', language='ENG')
>>> 24
```

## Security

Mathparse does not employ the use of Python's [`eval` function](https://docs.python.org/3/library/functions.html#eval) when evaluating provided mathematical expressions. This is a measure to prevent arbitrary code execution vulnerabilities. See https://mathparse.chatterbot.us/postfix/ for additional details.

Mathparse is a standalone Python package and requires zero dependencies to function.

## Language Support

The language parameter must be set in order to evaluate an equation that uses word operators.
The language code should be a valid [ISO 639-2](https://www.loc.gov/standards/iso639-2/php/code_list.php) language code.

## Installation

```bash
pip install mathparse
```

## Documentation

See the full documentation at https://mathparse.chatterbot.us

## Changelog

See [release notes](https://github.com/gunthercox/mathparse/releases) for changes.
