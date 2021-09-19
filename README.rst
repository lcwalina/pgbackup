pgbackup
========

CLI for backup remote PostgreSQL database either locally or to S3

Installation
------------

1. Ensure, that ``pip`` and ``pipenv`` are installed.
2. Clone repository: ``git clone git@github.com:sth/pgbackup``
3. ``cd`` into the repo.
4. Fetch development dependencies ``make install``
5. Activate virtualenv ``pipenv shell``

Usage
-----

Pass in a full database URL, the storage driver and the destination.

S3 example w/ bucket name:

::

    $ pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups

Local example w/ local path

::

    $ pgbackup postgres://bob@example.com:5432/db_one --driver local /var/local/my_db/backups/dump.sql

Running tests
-------------

Run test locally using ``make`` if virtualenv is active:

::

    $ make

If virtualenv isn't active then use:

::

    $ pipenv run make

