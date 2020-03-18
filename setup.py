from setuptools import setup
import os

version = '0.1.0'

with open("./README.md") as fd:
    long_description = fd.read()

setup(
    name = "voxelmorph",
    version = version,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.6",

    ]



)