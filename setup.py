#!/usr/bin/env python

from setuptools import setup, find_packages

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
      packages=find_packages(),
      classifiers=[
          "Programming Language :: Python",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ]
      )
