
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(name='vulminator',
      version=version,
      description="vulnerability feed downloader and importer",
      long_description=open("README.md").read(),
     
      author='Gregory Gallaway',
      author_email='greg4444@gmail.com',
      url='https://github.com/gregorylee/dart_interview',
      packages=find_packages(exclude=['ez_setup']),
      install_requires=[
          'setuptools',
          'elasticsearch',
          'feedparser'
                ],
      entry_points= {'console_scripts':['vulminator=vulminator.vulminator:main']}
      )