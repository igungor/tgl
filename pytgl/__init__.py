# -*- coding: utf-8 -*-


"""
    pytgl
    ~~~~~~~~~
    CFFI-based TGL bindings for Python. See README for details.
    :copyright: Copyright 2014 by Goekcen Eraslan
    :license: LGPL
"""

from cffi import FFI

from . import constants


VERSION = '0.0.1'

TGL_LIB = 'libtgl.so'

ffi = FFI()
ffi.cdef(constants._TGL_HEADERS)
tgl = ffi.dlopen(TGL_LIB)

from .constants import *
