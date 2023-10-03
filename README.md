[![Python application](https://github.com/Markel-Kaluhin/python-bootstrap-template/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/Markel-Kaluhin/python-bootstrap-template/actions/workflows/build.yml)
![Tests Pass Badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/Markel-Kaluhin/e8d23650144c1dd611a941789d52721a/raw/python-bootstrap-template__tests_passed.json)
![Linters Pass Badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/Markel-Kaluhin/e8d23650144c1dd611a941789d52721a/raw/python-bootstrap-template__linters_passed.json)
![Coverage Badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/Markel-Kaluhin/e8d23650144c1dd611a941789d52721a/raw/python-bootstrap-template__coverage.json)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/Markel-Kaluhin/python-bootstrap-template)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)


# Python Bootstrap Template

This is a template for all my future repositories primarily containing Python code.

Here, I intend to keep up-to-date all my essential and favorite linters and other tools necessary for productive and comfortable work.

# Prerequisites

To work with this repo you need to know how to work with [Pipenv](https://pipenv.pypa.io/en/latest/) package manager

Here I utilized Python version 3.11.5 if you want to change target version you'd need to change Python version in:
1. [Pipfile](Pipfile) to change used version of Python
1. [pyproject.toml](pyproject.toml) to specify target `Python` version for `Black` linter
1. [setup.cfg](setup.cfg) to specify target `Python` version for `Mypy`

# Default commands

All the commands execute with the prefix `pipenv run`, like `pipenv run unit` to run the unittests

The list of the following commands was implemented by default:

1. `unit` - to run unittests
1. `coverage` - to calculate the lines coverage
1. `lint` - to apply the linters to the codebase
1. `app` - to run application
