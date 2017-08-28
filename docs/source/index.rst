R5 Documentation
================

.. toctree::
   reference

   .. image:: https://travis-ci.org/benureau/r5.svg?branch=master
      :target: https://travis-ci.org/benureau/r5
      :alt: unit tests
   .. image:: https://codecov.io/gh/benureau/r5/branch/master/graph/badge.svg
      :target: https://codecov.io/gh/benureau/r5
      :alt: test coverage
   .. image:: https://readthedocs.org/projects/r5-/badge/?version=latest
      :target: http://r5-.readthedocs.io/en/latest/?badge=latest
      :alt: documentation
   .. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.848221.svg
      :target: https://doi.org/10.5281/zenodo.848221
      :alt: doi

This is the documentation for the code of the article "Re-run, Repeat, Reproduce, Reuse, Replicate: Transforming Code into Scientific Contributions"
by `Fabien C. Y. Benureau`__ and `Nicolas P. Rougier`__. This code is meant as an example of a :math:`\textrm{R}^4` implementation: re-runnable, repeatable, reproducible, and reusable.

__ https://fabien.benureau.com
__ https://www.labri.fr/perso/nrougier/

This code exposes two central functions, :func:`r5.walk` that generates the walk, and :func:`r5.walk_full` that generates the walk and returns it with full provenance data (parameters, python version, platform, git hash):

.. autofunction:: r5.walk

.. autofunction:: r5.walk_full


Re-runnable
-----------

The :mod:`r5` code requires Python 3. The preferred installation method is to clone the existing git repository, and run the code from there. This is necessary to retrieve the git part of the provenance data::

    git clone https://github.com/benureau/r5
    cd r5
    python setup.py develop

We use ``python setup.py develop`` rather than ``python setup.py install`` to avoid divorcing the code from the version control system. There are ways to record the git data at installation, such as the `versioneer`_ package, but we don't use it here to keep things as simple as possible.

.. _versioneer: https://pypi.python.org/pypi/versioneer/

A test is then provided to check that the code is indeed re-runnable::

    pytest r5/tests/test_rerunnable.py

An example is also included in the examples folder::

    python examples/example.py


Repeatable
----------

Random seeds for the random number generator are explicitly set with each invocation of :func:`r5.walk` (the seed is 1 if none is provided).
You can explicitly verify that the code produce repeatable results with::

    pytest tests/test_repeatable.py


Reproducible
------------

The main thing that makes the code reproducible is the addition of provenance data tracking to record the context in which the walk is computed. This provenance data contains details about the computer platform and the python version, the packages installed and their versions, the version of the code (git SHA1 hash) and the parameters used to generate the results.

.. autofunction:: r5.provenance

It is assumed that the code is executed in its git repository, with no uncommitted files. That makes
the SHA-1 of the current commit a full description of the state of the code used to compute the
results. If the repository is dirty (uncommitted changes or untracked files are present) or unavailable (if the
package was installed with :code:`python setup.py install` for instance), an error is raised, and the user
is informed that it must explicitly bypass the requirement of a clean git repository by set the :code:`dirty` argument to true in the :func:`r5.walk_full` function.

Such "dirty" runs of the code might be useful during development and debugging, but they should not
be used to produce published results.

To test reproducibility, the code checks if it generates the same result that previous versions of the
code. If the code is purposefully changed to modify behavior, then the test data must be regenerated, by executing the ``tests/generate_testdata.py`` file. If not, the test catches unintentional semantic changes to the code. You can run the test with::

    pytest tests/test_reproducible.py

Furthermore, the code is hosted via the Zenodo_ platform with a DOI, ensuring it remains reachable and available for the foreseeable future.

.. _Zenodo: https://zenodo.org/


Reusable
--------

This repository was designed to function as a solid code foundation to start new projects, with
all the battery of the :math:`\textrm{R}^4` code included. Care has been given to create simple and
well-documented code, that is easy to install and use.

A `setup.py` file is provided, along with a `requirement.txt` file that list the dependencies one should install. Examples and tests are included, and the latter are automatically evaluated for each commit pushed to the GitHub
repository using the Travis_ continuous integration service.

.. _Travis: https://travis-ci.org/benureau/r5

You can, prior to committing the files, run those tests efficiently with::

    pytest

at the root of the repository. You can further examine how completely the tests cover the code by running::

    pytest --cov

The coverage is full for the ``walker.py`` file where the core code resides; it is partial for ``provenance.py``, as some cases of the git repository being dirty or absent are not tested.

This code is certainly not perfect, and would it be, it would not remain that way as the rest of the software stack and computer technology shift around it. Tools such as containers_ may help long-term rerunnability and provenance tracking once the technology matures and takes into accounts the specific constraints of long-term scientific reproducibility.

.. _containers: https://www.opencontainers.org/

Do not hesitate to copy or fork this code or take just bits of it to make your current or next projects (hopefully) better. If stumbling on a problem, drop us an `issue on GitHub`__.

__ https://github.com/benureau/r5/issues
