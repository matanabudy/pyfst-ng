#!/bin/bash
python3 expand_tpl.py fst/_fst.pyx.tpl fst/types.yml fst/_fst.pyx
python3 expand_tpl.py fst/libfst.pxd.tpl fst/types.yml fst/libfst.pxd
cython --cplus fst/libfst.pxd
cython --cplus fst/_fst.pyx
