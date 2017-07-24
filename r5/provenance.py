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
            'timestamp': datetime.utcnow().isoformat()+'Z',  # Z stands for UTC
           }
