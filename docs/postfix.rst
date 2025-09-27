Postfix
=======

The postfix notation, also known as `Reverse Polish Notation (RPN)`_, is a mathematical notation in which every operator follows all of its operands.
It is used in mathparse to evaluate expressions efficiently.

Additionally, mathparse does not employ the use of Python's :py:func:`eval` function when evaluating provided mathematical expressions.
This is a measure to prevent arbitrary code execution vulnerabilities.

.. _`Reverse Polish Notation (RPN)`: https://en.wikipedia.org/wiki/Reverse_Polish_notation
