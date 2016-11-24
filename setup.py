#!/usr/bin/env python

from setuptools import setup


# Dynamically retrieve the version information from the chatterbot module
MATHPARSE = __import__('mathparse')
VERSION = MATHPARSE.__version__
AUTHOR = MATHPARSE.__author__
AUTHOR_EMAIL = MATHPARSE.__email__
URL = MATHPARSE.__url__
DOC = MATHPARSE.__doc__

setup(
    name='mathparse',
    version=VERSION,
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DOC,
    packages=[
        'mathparse',
    ],
    package_dir={'mathparse': 'mathparse'},
    license='MIT',
    zip_safe=True,
    platforms=['any'],
    keywords=['mathparse'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Text Processing :: General',
        'Topic :: Text Processing :: Linguistic',
        'Programming Language :: Python',
    ],
    test_suite='tests'
)
