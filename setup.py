from setuptools import setup, find_packages

setup(
    name = 'calculator',
    version = '0.1', 
    packages = find_packages(exclude=['tests*']),
    license = 'MIT',
    description = 'example calculator package', 
    long_description = open('README.md').read(),
    install_requires = ['numpy'],
    url = 'url',
    author = 'Claudia', 
    author_email = 'email'
)