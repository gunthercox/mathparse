# mathparse

**A secure, multilingual mathematical expression evaluator for Python**

`mathparse` is a Python library that safely parses and evaluates mathematical expressions from strings, supporting both numeric operators and natural language words across 13+ languages. Unlike Python's dangerous `eval()` function, mathparse provides a secure, zero-dependency solution for evaluating user-provided mathematical expressions.

## Why mathparse?

✅ **Security First** - Never uses `eval()`, protecting against arbitrary code execution  
✅ **Multilingual Support** - Parse math in English, Spanish, French, German, Chinese, and 8+ more languages  
✅ **Zero Dependencies** - Pure Python implementation with no external requirements  
✅ **Natural Language** - Understands "fifty times twenty plus ten" alongside standard notation  
✅ **Production Ready** - Used in chatbots, calculators, voice assistants, and educational applications  
✅ **Well Tested** - Comprehensive test suite ensuring reliability

## Quick Examples

```python
from mathparse import mathparse

# Standard numeric expressions
mathparse.parse('50 * (85 / 100)')
>>> 42.5

# Natural language in English
mathparse.parse('one hundred times fifty four', language='ENG')
>>> 5400

# Mixed notation
mathparse.parse('(seven * nine) + 8 - (45 plus two)', language='ENG')
>>> 24

# Other languages (French, Spanish, German, Chinese, etc.)
mathparse.parse('cinq plus trois', language='FRE')
>>> 8

mathparse.parse('cinco más tres', language='ESP')
>>> 8
```

## Use Cases

- 🤖 **Chatbots & Voice Assistants** - Parse natural language math queries
- 🧮 **Calculator Applications** - Build safe calculators that accept text input
- 📚 **Educational Software** - Evaluate student-provided math expressions
- 🌐 **Multilingual Apps** - Support math parsing in users' native languages
- 🔐 **Secure Code Evaluation** - Replace dangerous `eval()` calls with safe parsing
- 📊 **Data Processing** - Extract and calculate values from natural language text

## Security: Why Not eval()?

Python's `eval()` function executes arbitrary code, creating severe security vulnerabilities:

```python
# DANGEROUS - Never do this with user input!
eval("__import__('os').system('rm -rf /')")  # Deletes files
eval("__import__('requests').get('evil.com')")  # Network access
```

**mathparse is the safe alternative:**

| Feature | eval() | mathparse |
|---------|--------|-----------|
| Mathematical expressions | ✅ | ✅ |
| Arbitrary code execution | ⚠️ **YES - DANGEROUS** | ❌ No |
| File system access | ⚠️ **YES - DANGEROUS** | ❌ No |
| Network access | ⚠️ **YES - DANGEROUS** | ❌ No |
| Import statements | ⚠️ **YES - DANGEROUS** | ❌ No |
| Security risk | 🔴 **CRITICAL** | 🟢 Safe |
| Dependencies | 0 | 0 |
| Natural language support | ❌ No | ✅ Yes |
| Multilingual | ❌ No | ✅ 13+ languages |

mathparse uses [postfix (Reverse Polish) notation](https://mathparse.chatterbot.us/postfix/) internally, ensuring only valid mathematical operations are performed. See our [security documentation](https://mathparse.chatterbot.us/postfix/) for technical details.

## Performance

- **Fast**: Simple numeric expressions parse in microseconds
- **Efficient**: Minimal memory footprint, suitable for high-volume applications
- **Scalable**: Linear time complexity for expression evaluation

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
