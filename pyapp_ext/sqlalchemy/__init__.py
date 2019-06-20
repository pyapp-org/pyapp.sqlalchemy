"""
pyApp - SQLAlchemy Extension

This extension provides a factory method for connecting to a SQL RDBMS.

"""
from .factory import *


class Extension:
    """
    pyApp SQLAlchemy Extension
    """
    default_settings = ".default_settings"
    checks = ".checks"

    @staticmethod
    def ready():
        from pyapp.injection import register_factory
        register_factory(Session, get_session)
        register_factory(Connection, get_connection())
        register_factory(Engine, get_engine)
