import sys
import os
import platform
from datetime import datetime

import pip
import git


def provenance(dirty=False):
    """Return provenance data about the execution environment."""
    return {'python'   : {'implementation': platform.python_implementation(),
                                'version' : platform.python_version_tuple(),
                                'compiler': platform.python_compiler(),
                                'branch'  : platform.python_branch(),
                                'revision': platform.python_revision()},
            'platform'  : platform.platform(),
            'packages'  : list(pip.commands.freeze.freeze()), # list of installed packages
            'git_info'  : git_info(dirty_allowed=dirty),
            'timestamp' : datetime.utcnow().isoformat()+'Z',  # Z stands for UTC
           }

def git_info(dirty_allowed=False):
    """Try to retrieve the git diff."""
    try: # are we in a git repository?
        dotdot = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        repo = git.Repo(dotdot, search_parent_directories=False)
        if (not dirty_allowed) and repo.is_dirty():
            print('error: git is dirty, aborting.')
            sys.exit(1)

        return {'hash': repo.head.object.hexsha, 'dirty': repo.is_dirty(),
                'git_version': str(pip.git.Git().get_git_version())}

    except git.exc.InvalidGitRepositoryError as e: # not in a git repo
        if not dirty_allowed:
            print('error: git repository not found, aborting.')
            sys.exit(1)

        return {'warning': 'git repository not found during execution.'}
