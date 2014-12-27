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

def dlopen(ffi, names):
    """Try various names for the same library, for different platforms."""
    for name in names:
        try:
            return ffi.dlopen(name)
        except OSError:
            pass
    # Re-raise the exception.
    return ffi.dlopen(names[0])

TGL_LIBS = ['libtgl.so', 'libtgl.0.dylib']

ffi = FFI()
ffi.cdef(constants._TGL_HEADERS)
tgl = dlopen(ffi, TGL_LIBS)

from .constants import *
