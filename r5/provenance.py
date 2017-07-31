import os
import platform
from datetime import datetime

from . import _version


def provenance():
    """Return provenance data about the execution environment."""
    return {'python'   : {'implementation': platform.python_implementation(),
                                'version' : platform.python_version_tuple(),
                                'compiler': platform.python_compiler(),
                                'branch'  : platform.python_branch(),
                                'revision': platform.python_revision()},
            'platform' : platform.platform(),
            'git_info' : _version.get_versions(),
            'git_diff' : git_diff(),
            'timestamp': datetime.utcnow().isoformat()+'Z',  # Z stands for UTC
           }

def git_diff():
    """Try to retrieve the git diff."""
    import git
    try: # if the package is installed or out of it git repository, this will fail.
        here = os.path.abspath(os.path.dirname(__file__))
        repo = git.Repo(here, search_parent_directories=True)
        diff = repo.git.diff(repo.head.commit.tree)
    except git.exc.InvalidGitRepositoryError as e:
        # FIXME detect if code is dirty
        diff = 'error: could not retrieve diff from git ({}).'.format(e)
    return diff
