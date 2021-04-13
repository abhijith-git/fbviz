from codecs import open
import os
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

VERSION = '0.0.1'
DESCRIPTION = 'Football visualizer'
#LONG_DESCRIPTION = DESCRIPTION
URL = 'https://github.com/abhijith-git/fbviz'

# Setting up
setup(
    name="fbviz",
    version=VERSION,
    author="Abhijith Chandradas",
    author_email="<abhijith.chandradas@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=README,
    url=URL,
    license='MIT',
    packages=find_packages(exclude=["tests", "*.tests", "*.tests.*", "tests.*"]),
    install_requires=['matplotlib', 
                      'pandas', 
                      'numpy'],
    keywords=['python', 
              'options', 
              'finance', 
              'opstrat', 
              'data visualization', 
              'stock market'],
    classifiers=[
            "Development Status :: 1 - Planning",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Intended Audience :: Science/Research",
            "Intended Audience :: Financial and Insurance Industry",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Topic :: Scientific/Engineering :: Visualization",
            'Topic :: Scientific/Engineering :: Information Analysis',
            "Topic :: Office/Business :: Financial :: Investment",
            "Topic :: Office/Business :: Financial",
            "Programming Language :: Python :: 3"]
)