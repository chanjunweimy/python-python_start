========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-python_start/badge/?style=flat
    :target: https://readthedocs.org/projects/python-python_start
    :alt: Documentation Status


.. |travis| image:: https://travis-ci.org/chanjunweimy/python-python_start.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/chanjunweimy/python-python_start

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/chanjunweimy/python-python_start?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/chanjunweimy/python-python_start

.. |requires| image:: https://requires.io/github/chanjunweimy/python-python_start/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/chanjunweimy/python-python_start/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/chanjunweimy/python-python_start/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/chanjunweimy/python-python_start

.. |version| image:: https://img.shields.io/pypi/v/python-start.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/python-start

.. |commits-since| image:: https://img.shields.io/github/commits-since/chanjunweimy/python-python_start/v0.0.1.svg
    :alt: Commits since latest release
    :target: https://github.com/chanjunweimy/python-python_start/compare/v0.0.1...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/python-start.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/python-start

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/python-start.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/python-start

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/python-start.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/python-start


.. end-badges

experimenting this library

* Free software: MIT license

Installation
============

::

    pip install python-start

Documentation
=============


https://python-python_start.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
