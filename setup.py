#!/usr/bin/env python


from setuptools import setup

setup(
    name='geocrypt',
    version='1.0.0',
    install_requires=[],
    author='Spatial Current Developers',
    author_email='opensource@spatialcurrent.io',
    license='BSD License',
    url='https://github.com/spatialcurrent/geocrypt/',
    keywords='python',
    description='A Python library for hashing common geospatial objects.',
    long_description=open('README.rst').read(),
    download_url="https://github.com/spatialcurrent/geocrypt/zipball/master",
    packages=["geocrypt"],
    package_data={'': ['LICENSE', 'NOTICE'], 'geocrypt': ['*.pem']},
    package_dir={'geocrypt': 'geocrypt'},
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
