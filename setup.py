#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import yaml

from setuptools import find_packages
from setuptools import setup

with open('wazo/plugin.yml') as file:
    metadata = yaml.load(file)

setup(
    name=metadata['name'],
    version=metadata['version'],
    description=metadata['display_name'],
    author=metadata['author'],
    url=metadata['homepage'],

    packages=find_packages(),
    include_package_data=True,
    package_data={
        'wazo_calld_application_continue': ['api.yml']
    },
    entry_points={
        'wazo_calld.plugins': [
            'continue = wazo_calld_application_continue.plugin:Plugin'
        ]
    }
)
