#File for the creation of the shared object

from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = (cythonize("cy_sort.pyx"))

setup(ext_modules = exts)
