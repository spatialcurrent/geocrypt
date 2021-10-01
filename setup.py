# -*- coding: utf-8 -*-
from distutils.core import setup

VERSION = '0.1.0'
URL = 'https://github.com/spatialcurrent/geocrypt'

setup(
    author='Spatial Current Developers',
    author_email='opensource@spatialcurrent.io',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    description='A Python library for hashing common geospatial objects.',
    download_url="https://github.com/spatialcurrent/geocrypt/zipball/master",
    name='geocrypt',
    include_package_data=True,
    install_requires=[],
    license='BSD License',
    long_description=open('README.rst').read(),
    keywords='python',
    maintainer='Spatial Current Developers',
    maintainer_email='opensource@spatialcurrent.io',
    packages=[
        "geocrypt"
    ],
    package_data={
        '': ['LICENSE', 'requirements.txt'],  # noqa
        '': ['*.*'],  # noqa
    },
    python_requires='>=3.9',
    url=URL,
    version=VERSION,
    zip_safe=False
)
