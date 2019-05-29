##################
pyApp - SQLAlchemy
##################

*Let us handle the boring stuff!*

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
      :alt: Once you go Black...

.. image:: https://api.codeclimate.com/v1/badges/0a86755f39f0416fbd1e/maintainability
   :target: https://codeclimate.com/github/pyapp-org/pae.sqlalchemy/maintainability
   :alt: Maintainability

This extension provides a `Connection` and `Session` factory for SQLAlchemy to
allow database connections to be configured via pyApp settings. 

`Engine` instances are created from a singleton factory to ensure that 
connection pooling is utilised.

The extension also provides checks to confirm the settings are correct and
that the application is able to connect to the database host.


Installation
============

Install using *pip*::

    pip install pae.sqlalchemy

Install using *pipenv*::

    pipenv install pae.sqlalchemy


Add `pae.sqlalchemy` into the `EXT` list in your applications 
`default_settings.py`.

Add the `DATABASE_ENGINES` block into your runtime settings file::

    DATABASE_ENGINES = {
        "default": {
            "url": "postgres://user:pass@host:port/database",
        },
    }


.. note::

    The URI is a defined by SQLAlchemy see the
    `documentation <https://docs.sqlalchemy.org/en/13/core/engines.html>`_. In addition to
    the url any argument that can be provided to `sqlalchemy.engines.create_engine` can be
    provided.


Usage
=====

The following example creates both `Connection` and `Session` instances::

    from pae.sql_alchemy import get_connection, get_session

    # Get connection from default connection pool
    cnn = get_connection()

    # Get connection from an alternate pool
    session = get_session("Alternate")


API
===

`pae.sqlalchemy.get_engine(default: str = None) -> Engine`

    Get named `Engine` instance (singleton)


`pae.sqlalchemy.get_connection(default: str = None) -> Connection`

    Get named `Connection` instance.


`pae.sqlalchemy.get_raw_connection(default: str = None)`

    Get named *raw* connection, this is the underlying Python DBAPI object.


`pae.sqlalchemy.get_session(default: str = None) -> Session`

    Get named `Session` instance.
