"""
Revolt API Wrapper
~~~~~~~~~~~~~~~~~~~

A basic wrapper for the Revolt API.

:copyright: (c) 2024-present MCausc78
:license: MIT, see LICENSE for more details.

"""

__title__ = 'pyvolt'
__author__ = 'MCausc78'
__license__ = 'MIT'
__copyright__ = 'Copyright 2024-present MCausc78'
__version__ = '1.0.1'

from . import (
    abc as abc,
    routes as routes,
    utils as utils,
)

from .adapter import *
from .authentication import *
from .base import *
from .bot import *
from .cache import *
from .cdn import *
from .channel import *
from .client import *
from .context_managers import *
from .core import *
from .discovery import *
from .embed import *
from .emoji import *
from .enums import *
from .errors import *
from .events import *
from .flags import *
from .http import *
from .instance import *
from .invite import *
from .message import *
from .parser import *
from .permissions import *
from .read_state import *
from .safety_reports import *
from .server import *
from .settings import *
from .shard import *
from .state import *
from .user import *
from .utils import *
from .webhook import *

import typing

if typing.TYPE_CHECKING:
    from . import raw as raw


class _VersionInfo(typing.NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: typing.Literal['alpha', 'beta', 'candidate', 'final']
    serial: int


version_info: typing.Final[_VersionInfo] = _VersionInfo(
    major=1,
    minor=0,
    micro=1,
    releaselevel='final',
    serial=0,
)


del typing
