#! /usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup

__version__ = "0.0.3"

setup(
    name="Bashutils",
    version=__version__,
    packages=["bashutils", "bashutils.test"],

    author='Olivier BLIN',
    author_email='olivier.oblin@gmail.com',
    description="Bash colors management and log system",
    long_description=open('README.rst').read(),
    keywords="bash color log",
    url='https://github.com/OlivierB/Bashutils.git',
    license='GPLv3',
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
    ],
)
