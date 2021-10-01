geocrypt
==============

.. image:: https://circleci.com/gh/spatialcurrent/geocrypt.svg?style=svg
    :target: https://circleci.com/gh/spatialcurrent/geocrypt

.. image:: https://img.shields.io/pypi/v/geocrypt.svg
    :target: https://pypi.python.org/pypi/geocrypt

.. image:: https://readthedocs.org/projects/geocrypt/badge/?version=main
        :target: http://geocrypt.readthedocs.org/en/latest/
        :alt: Main Documentation Status

Description
-----------------

A Python library for hashing common geospatial objects.

Installation
-----------------

Install via PyPI_ with:

.. _PyPI: https://pypi.python.org/pypi

.. code-block:: bash

    pip install geocrypt

Or install directly from GitHub_ with:

.. _GitHub: https://github.com/

.. code-block:: bash

    pip install git+git://github.com/spatialcurrent/geocrypt.git@main

Usage
-----------------

Below are some simple use cases.  See test.py for more use cases.

.. code:: python

   from geocrypt import geocrypt

   digest_a = geocrypt.hash({"type": "lonlat", "value": [-77.042999267578125, 38.922558058625356]})
   # digest_a == "cc0a149fd1387a34412ee47cb08ab12b"

   digest_b = geocrypt.hash({"geometry": {"coordinates": [-77.042999267578125, 38.922558058625356], "type": "Point"}, "id": 1, "properties": {"addr:street": "18th Street Northwest"}, "type": "Feature"})
   # digest_b == "cc0a149fd1387a34412ee47cb08ab12b"

   # digest_a == digest_b

By default, the md5 hash algorithm is used, but other algorithms can be selected, too.

.. code:: python

    geocrypt.hash({"type": "lonlat", "value": [-77.042999267578125, 38.922558058625356]}, algorithm="sha512")

You can also round all coordinates to a given number of decimal places.  5 is a standard number to round to for online maps.  By rounding to 5 decimal places, you mitigate floating point errors that might lead 2 different hashes for locations that are the same for all intents and purposes, such as [-77.042999267578125, 38.922558058625356] and [-77.042999299999, 38.922558099999].

.. code:: python

    geocrypt.hash({"type": "lonlat", "value": [-77.042999267578125, 38.922558058625356]}, decimals=5)

Testing
-----------------

For unit tests, run the following command from the project root folder:

.. code:: shell

    python -m unittest -v geocrypt.test

Contributing
-----------------

`Spatial Current, Inc.`_ is currently accepting pull requests for this repository.  We'd love to have your contributions!  Please see `Contributing.rst`_ for how to get started.

.. _`Spatial Current, Inc.`: https://spatialcurrent.io
.. _Contributing.rst: https://github.com/spatialcurrent/geocrypt/blob/main/CONTRIBUTING.rst

License
-----------------

This work is distributed under the **MIT License**.  See **LICENSE** file.
