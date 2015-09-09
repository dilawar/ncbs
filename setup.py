import os
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md") as f:
    readme = f.read()
classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    ]

setup(
    name = "ncbs",
    version = "0.0.1",
    description = "Useful scripts for NCBS Bangalore",
    long_description = readme,
    packages = ["scripts" ],
    package_data = { },
    install_requires = [ ],
    author = "Dilawar Singh",
    author_email = "dilawars@ncbs.res.in",
    url = "http://github.com/dilawar/ncbs",
    license='MIT',
    classifiers=classifiers,

    entry_points = {
        'console_scripts': ['ncbs=ncbs:main'],
        }
)
