"""
PyApp - SQLAlchemy Extension

This extension provides a factory method for connecting to a SQL RDBMS.

"""
from .factory import *


class Extension:
    __default_settings__ = ".default_settings"
    __checks__ = ".checks"
