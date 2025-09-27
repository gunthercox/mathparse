Installation
============

mathparse can be installed using pip:

.. code-block:: shell

    pip install mathparse


Usage
=====

.. code-block:: python

    from mathparse import mathparse

    mathparse.parse('50 * (85 / 100)')
    >>> 42.5

    mathparse.parse('one hundred times fifty four', mathparse.codes.ENG)
    >>> 5400

    mathparse.parse('(seven * nine) + 8 - (45 plus two)', language='ENG')
    >>> 24


.. note::

    The language parameter must be set in order to evaluate an equation that uses word operators.
    The language code should be a valid `ISO 639-2`_ language code.


Development
===========

To generate the documentation locally, clone the repository and install the development requirements:

.. code-block:: shell

    git clone https://github.com/gunthercox/mathparse.git
    cd mathparse
    pip install .[test]

Then, from the root of the repository, run:

.. code-block:: shell

    sphinx-build -nW -b dirhtml docs/ html/

You can then open the generated HTML files in the `html/` directory, or serve them using a command such as:

.. code-block:: shell

    python -m http.server --directory html 8000

.. _`ISO 639-2`: https://www.loc.gov/standards/iso639-2/php/code_list.php
