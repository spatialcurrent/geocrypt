geocrypt
==============

.. image:: https://travis-ci.org/spatialcurrent/geocrypt.png
    :target: https://travis-ci.org/spatialcurrent/geocrypt

.. image:: https://img.shields.io/pypi/v/geocrypt.svg
    :target: https://pypi.python.org/pypi/geocrypt

.. image:: https://readthedocs.org/projects/geocrypt/badge/?version=master
        :target: http://geocrypt.readthedocs.org/en/latest/
        :alt: Master Documentation Status

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

    pip install git+git://github.com/spatialcurrent/geocrypt.git@master

Usage
-----------------


.. code:: python

   from geocrypt import geocrypt

   digest_a = geocrypt.hash({"type": "lonlat", "value": [-77.042999267578125, 38.922558058625356]})
   # digest_a == "cc0a149fd1387a34412ee47cb08ab12b"

   digest_b = geocrypt.hash({"geometry": {"coordinates": [-77.042999267578125, 38.922558058625356], "type": "Point"}, "id": 1, "properties": {"addr:street": "18th Street Northwest"}, "type": "Feature"})
   # digest_b == "cc0a149fd1387a34412ee47cb08ab12b"

   # digest_a == digest_b

Testing
-----------------

For unit tests, run the following command from the project root folder:

.. code:: shell

    python -m unittest -v geocrypt.test

Contributing
-----------------

`Spatial Current, Inc.`_ is currently accepting pull requests for this repository.  We'd love to have your contributions!  Please see `Contributing.rst`_ for how to get started.

.. _`Spatial Current, Inc.`: https://spatialcurrent.io
.. _Contributing.rst: https://github.com/spatialcurrent/geocrypt/blob/master/CONTRIBUTING.rst

License
-----------------

This work is distributed under the **MIT License**.  See **LICENSE** file.
