#!/usr/bin/env python

from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(name='bluerobotics-tsys01',
    version='0.0.1',
    description='A python module for the TSYS01 digital temperature sensor',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Blue Robotics',
    author_email='support@bluerobotics.com',
    url='https://www.bluerobotics.com',
    packages=["tsys01"],
    package_data={ "tsys01": ["tsys01.meta"]},
    entry_points={
        'console_scripts': [
            'tsys01-report=tsys01.report:main',
            'tsys01-test=tsys01.test:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'smbus',
    ]
)
