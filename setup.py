import sys
import os
from distutils.core import setup
from distutils.extension import Extension

INC, LIB = [], []

if not os.path.exists('fst/_fst.cpp'):
    os.system('./prepare_fst_cpp.sh')

# MacPorts
if sys.platform == 'darwin' and os.path.isdir('/usr/local/lib'):
    INC.append('/usr/local/include')
    LIB.append('/usr/local/lib')

ext_modules = [
    Extension(name='fst._fst',
              sources=['fst/_fst.cpp'],
              libraries=['fst'],
              extra_compile_args=['--std=c++11', '-g', '-O2'],
              include_dirs=INC,
              library_dirs=LIB)
]

long_description = """
pyfst
=====

A Python interface for the OpenFst_ library.

.. _OpenFst: https://www.openfst.org

- Documentation:https:///pyfst.github.io
- Source code: https://github.com/vchahun/pyfst

Example usage::

    import fst

    t = fst.Transducer()

    t.add_arc(0, 1, 'a', 'A', 0.5)
    t.add_arc(0, 1, 'b', 'B', 1.5)
    t.add_arc(1, 2, 'c', 'C', 2.5)

    t[2].final = 3.5

    t.shortest_path() # 2 -(a:A/0.5)-> 1 -(c:C/2.5)-> 0/3.5 

"""

setup(
    name='pyfst',
    version='1.7.9',
    url='https://pyfst.github.io',
    author='Victor Chahuneau',
    description='A Python interface to OpenFst.',
    long_description=long_description,
    classifiers=['Topic :: Text Processing :: Linguistic',
                 'Programming Language :: Cython',
                 'Programming Language :: C++',
                 'Intended Audience :: Education',
                 'Intended Audience :: Science/Research'],
    install_requires=['pyyaml', 'cython'],
    packages=['fst'],
    ext_modules=ext_modules
)
