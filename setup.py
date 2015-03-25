"""
Setup.

Installs console script and deps.
"""
from setuptools import setup


setup(
    name='datasit-graphite',
    version='1.0',
    description='Graph your Datasift account metrics in Graphite.',
    long_description=open('README.md').read(),
    author='Lex Toumbourou',
    author_email='lextoumbourou@gmail.com',
    url='https://github.com/lextoumbourou/datasift-graphite',
    license='MIT License',
    install_requires=['datasift'],
    entry_points={
        'console_scripts': ['datasift-graphite = datasift_graphite:main'],
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ]
)