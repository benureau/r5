R5 Documentation
================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

This is the documentation for the code of the article "Re-run, Repeat, Reproduce, Reuse, Replicate: Transforming Code into Scientific Contributions"
by Fabien C. Y. Benureau and Nicolas P. Rougier. This code is meant as an example of a :math:`\textrm{R}^4` implementation:
re-runnable, repeatable, reproducible, and reusable.

This code exposes two central functions, :func:`r5.walk` that generate the walk, and :func:`r5.walk_full` that generate the walk and returns it with full provenance data (parameters, python version, plaform, git hash):

.. autofunction:: r5.walk

.. autofunction:: r5.walk_full


Re-runnable
-----------

The `r5` code requires Python 3. It can be installed with `pip`::

    pip install r5

You can also clone the git repository and install directly::

    git clone https://github.com/benureau/r5
    cd r5
    python setup.py install

If you wish to edit the code and test the changes without reinstalling it::

    python setup.py develop

A test is then provided to check that the code is indeed re-runnable::

    pytest r5/tests/test_rerunnable.py

An example is also included in the examples folder::

    python examples/example.py


Repeatable
----------

Random seeds for the random number generator are explicitely set with each invocation of :func:`r5.walk` (the seed is 1 if none is provided).
You can explicitely verify that the code produce repeatable results with::

    pytest tests/test_repeatable.py


Reproducible
------------

The main thing that makes the code reproducible is the addition of provenance data function to track the context in which the walk is computed. Along with the parameters used and details about the computer platform and the python version, version control (git) info is also recorded.

.. autofunction:: r5.provenance

It is assumed that the code is executed in its git repository, with no uncommited files. That makes
the SHA-1 of the current commit a full description of the state of the code used to compute the
results. If the repository is dirty (uncommited changes or untracked files) or unavailable (if the
package was installed with `python setup.py install` for instance), the user must explicitely bypass
the requirement of a clean git repository by set the `dirty` argument to true in the :func:`r5.walk_full` function.

To test reproducibility, the code test if it generate the same result that previous versions of the
code. You can run the test with::

    pytest tests/test_reproducible.py
