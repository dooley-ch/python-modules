from setuptools import setup, find_packages

setup(
    name='lib',
    description='Holds the demo classes',
    version='0.0.1',
    author='James Dooley',
    author_email='xxx@yyy.com',
    packages=find_packages(exclude=('test',)),
    url=''
)
