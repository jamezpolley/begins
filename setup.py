#!/usr/bin/env python
from setuptools import setup
import re
import sys

PYTHON3K = sys.version_info[0] > 2

setup(
    setup_requires=['pbr'],
    pbr=True,
    tests_require=['mock'] + ([] if PYTHON3K else ['unittest2']),
    test_suite="tests" if PYTHON3K else "unittest2.collector"
)
