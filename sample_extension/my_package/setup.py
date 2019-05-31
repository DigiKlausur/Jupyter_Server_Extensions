# -*- coding: utf-8 -*-


from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='my_module',
    version='0.1.0',
    description='My cool module',
    long_description=readme,
    author='Max Mustermann',
    author_email='m@x.com',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)