=========
mathparse
=========

.. image:: https://travis-ci.org/gunthercox/mathparse.svg?branch=master
    :target: https://travis-ci.org/gunthercox/mathparse

The mathparse library is a Python module designed to evaluate mathematical equations contained in strings.

Here are a few examples:

.. code-block:: python

   from mathparse import mathparse

   mathparse.parse('50 * (85 / 100)')
   >>> 42.5

   mathparse.parse('one hundred times fifty four', mathparse.codes.ENG)
   >>> 5400

   mathparse.parse('(seven * nine) + 8 - (45 plus two)', language='ENG')
   >>> 24

Installation
============

.. code-block:: bash

   pip install mathparse

Language support
================

The language parameter must be set in order to evaluate an equation that uses word operators.
The language code should be a valid `ISO 639-2`_ language code.

History
=======

See `release notes`_ for changes.

.. _`ISO 639-2`: https://www.loc.gov/standards/iso639-2/php/code_list.php
.. _`release notes`: https://github.com/gunthercox/ChatterBot/releases