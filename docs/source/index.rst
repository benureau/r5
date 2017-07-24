R5 Documentation
================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

This is the documentation for the code of the article "Re-run, Repeat, Reproduce, Reuse, Replicate: Transforming Code into Scientific Contributions"
by Fabien C. Y. Benureau and Nicolas P. Rougier. This code is meant as an example of a :math:`\textrm{R}^4` implementation:
re-runnable, repeatable, reproducible, and reusable.

This code exposes one central function, :func:`r5.walk`:

.. autofunction:: r5.walk


Re-runnable
-----------

The `r5` code requires Python 3. It can be installed with `pip`::

    pip install r5

You can also clone the git repository and install directly::

    git clone https://github.com/benureau/r5
    cd r5
    python setup.py install

A test is then provided to check that the code is indeed re-runnable::

    pytest tests/test_rerunnable.py

An example is also included in the examples folder::

    python examples/example.py



Repeatable
----------

Random seed for the random number generator are explicitely set with each invocation of :func:`r5.walk` (the seed is 1 if none is provided).
You can explicitely verify that the code produce repeatable results with::

    pytest tests/test_repeatable.py


Reproducible
------------

Reproducibility i
Random seed for the random number generator are explicitely set with each invocation of :func:`r5.walk` (the seed is 1 if none is provided).
You can explicitely verify that the code produce repeatable results with::

    pytest tests/test_repeatable.py


r5 module
---------

.. autofunction:: r5.provenance
