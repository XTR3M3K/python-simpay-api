#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='simpay-api',
    version='1.0',
    description='Python wrapper for Simpay API',
    author='XTR3M3K <mati.kucz65@gmail.com, Lenistwo',

    url='https://github.org/XTR3M3K/python-simpay-api',

    packages=['payments'],
    install_required=[
        'requests'
    ]
)
