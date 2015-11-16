
import os
from setuptools import setup
from pyneuronjs import __version__

# Utility function to read the README file.  
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'pyneuronjs',
    packages = ['pyneuronjs'],
    version = __version__,
    author = 'Kael Zhang',
    author_email = 'i@kael.me',
    description = ('The python middleware for neuron.js'),
    license = 'MIT',
    keywords = 'neuron.js middleware javascript loader facade',
    url = 'https://github.com/kaelzhang/pyneuronjs',
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
    ]
)
