R5 Documentation
================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

This is the documentation for the code of the article "Re-run, Repeat, Reproduce, Reuse, Replicate: Transforming Code into Scientific Contributions"
by `Fabien C. Y. Benureau`__ and `Nicolas P. Rougier`__. This code is meant as an example of a :math:`\textrm{R}^4` implementation: re-runnable, repeatable, reproducible, and reusable.

__ https://fabien.benureau.com
__ https://www.labri.fr/perso/nrougier/

This code exposes two central functions, :func:`r5.walk` that generates the walk, and :func:`r5.walk_full` that generates the walk and returns it with full provenance data (parameters, python version, plaform, git hash):

.. autofunction:: r5.walk

.. autofunction:: r5.walk_full


:math:`\textrm{R}^1`: Re-runnable
---------------------------------

The :mod:`r5` code requires Python 3. The preferred installation method is to clone the existing git repository, and run the code from there. This is necessary to retrieve the git part of the provenance data::

    git clone https://github.com/benureau/r5
    cd r5
    python setup.py develop

We use ``python setup.py develop`` rather than ``python setup.py install`` to, again, avoid divorcing the code from the version control system. There are ways to record the git data at installation, such as the `versioneer`_ package, but we don't use it here to keep things as simple as possible.

.. _versioneer: https://pypi.python.org/pypi/versioneer/

A test is then provided to check that the code is indeed re-runnable::

    pytest r5/tests/test_rerunnable.py

An example is also included in the examples folder::

    python examples/example.py


:math:`\textrm{R}^2`: Repeatable
--------------------------------

Random seeds for the random number generator are explicitely set with each invocation of :func:`r5.walk` (the seed is 1 if none is provided).
You can explicitely verify that the code produce repeatable results with::

    pytest tests/test_repeatable.py


:math:`\textrm{R}^3`: Reproducible
----------------------------------

The main thing that makes the code reproducible is the addition of provenance data tracking to record the context in which the walk is computed. This provenance data contains details about the computer platform and the python version, the packages installed and their versions, the version of the code (git SHA1 hash) and the parameters used to generate the results.

.. autofunction:: r5.provenance

It is assumed that the code is executed in its git repository, with no uncommited files. That makes
the SHA-1 of the current commit a full description of the state of the code used to compute the
results. If the repository is dirty (uncommited changes or untracked files are present) or unavailable (if the
package was installed with `python setup.py install` for instance), an error is raised, and the user
is informed that it must explicitely bypass the requirement of a clean git repository by set the `dirty` a
rgument to true in the :func:`r5.walk_full` function.

Such 'dirty' runs of the code might be useful during development and debugging, but they should not
be used to produce published results.

To test reproducibility, the code tests if it generates the same result that previous versions of the
code. If the code is purposfully changed to modify behavior, then the test must be adapated as well. If not, the test catches unintentional semantic changes to the code. You can run the test with::

    pytest tests/test_reproducible.py

Furthermore, the code is hosted via the Zenodo_ platform with a DOI, ensuring it remains reachable and available for the foreseable future.

.. _Zenodo: https://zenodo.org/


:math:`\textrm{R}^4`: Reusable
------------------------------



The code is provided with the present documentation. The code itself is properly documented, and the
interfaces one is expected to use have be made simple and easy to use. A `setup.py` file is provided,
along with a `requirement.txt` file that list the dependencies one should install. Tests and examples
accompagny the core code.
