#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import sys
sys.path.insert(0, 'gruffy')

setup(
    name='gruffy',
    version='0.3',
    description="Gruffy is Python implemetation of Gruff(Ruby Graphing Library)",
    long_description=open("README.rst").read(),
    license='MIT',
    author='Hideo Hattori',
    author_email='hhatto.jp@gmail.com',
    url='http://pypi.python.org/pypi/gruffy/',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: Unix',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Multimedia :: Graphics'],
    keywords="chart graph visualize",
    install_requires=['pgmagick'],
    packages=['gruffy'],
    zip_safe=False,
)
