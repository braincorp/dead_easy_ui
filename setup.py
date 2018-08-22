# ============================================================================
# Copyright 2017 BRAIN Corporation. All rights reserved. This software is
# provided to you under BRAIN Corporation's Beta License Agreement and
# your use of the software is governed by the terms of that Beta License
# Agreement, found at http://www.braincorporation.com/betalicense.
# ============================================================================

from setuptools import setup


setup(
    name='dead-easy-ui',
    author='Brain Corporation',
    author_email='peter.ed.oconnor@gmail.com',
    url='https://github.com/braincorp/dead_easy_ui',
    long_description='A package for streamline creation of console ui',
    version='0.0.1',
    scripts=[],
    packages=[],
    install_requires=[
        'pylint==1.9.2',
        'astroid==1.6.5',  # this is a pylint dependency. It is very sensitive to this version because of constant bugs.
        'py==1.5.2',
        'pep8==1.7.1',
        'pytest==3.6.3',
        'pytest-cache==1.0',
        'pytest-pep8==1.0.6',
        'pytest-cov==2.5.1',
        'pytest-xdist==1.19.1',
        'pytest-ordering==0.5',
        'pytest-pylint==0.11.0',
        'pytest-timeout==1.2.1',
        'future==0.16.0',  # python 3 compatibility
    ]
)
