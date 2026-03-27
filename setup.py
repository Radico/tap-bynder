#!/usr/bin/env python3
from setuptools import setup

setup(
    name="tap-bynder",
    version="0.1.1",
    description="Singer.io tap for extracting data",
    author="Simon Data",
    url="http://simondata.com",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_bynder"],
    python_requires=">=3.9",
    install_requires=[
        "singer-python==6.1.1",
        "requests==2.32.3",
        "pendulum==3.0.0",
        "tap-kit @ git+https://github.com/Radico/tap-kit.git@main",
        "requests_oauthlib==1.2.0",
    ],
    entry_points="""
    [console_scripts]
    tap-bynder=tap_bynder:main
    """,
    packages=["tap_bynder"],
    include_package_data=True,
)
