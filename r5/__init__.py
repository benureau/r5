import sys
import os
import argparse
import json

from .walker import walk, walk_full
from .provenance import provenance

# versioneer
__version__ = '0.5.0'


def test():
    """Run all the tests in the `tests/` directory using pytest """
    import pytest
    here = os.path.abspath(os.path.dirname(__file__))
    pytest.main([os.path.join(here, 'tests')])
