# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright (c) Treble.ai
#
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------

"""Simple Python ORM for PostgresDB."""

from .dbsession import DBConnection
from .dbsession import DatabaseObject

DBConnection
DatabaseObject

VERSION_INFO = (0, 5, 0, 'dev0')
__version__ = '.'.join(map(str, VERSION_INFO))
