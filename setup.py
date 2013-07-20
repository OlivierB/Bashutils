#! /usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup, find_packages

__version__ = "0.0.2"

setup(
    name="Bashutils",
    version=__version__,
    packages=find_packages(),

    author='Olivier BLIN',
    author_email='olivier.oblin@gmail.com',
    description="Bash colors management and log system",
    long_description=open('README.md').read(),
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
