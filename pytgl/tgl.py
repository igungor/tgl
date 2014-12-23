from . import ffi, tgl

from .callbacks import *

class TglState(object):
    def __init__(self):
        self._state = ffi.new('struct tgl_state *')
        self._update_cb = ffi.new('struct tgl_update_callback *')

    def set_callback(self, cb):
        tgl.tgl_set_callback(self._state, cb)

    def set_net_methods(self, m):
        tgl.tgl_set_net_methods(self._state, m)

    def set_timer_methods(self, m):
        tgl.tgl_set_timer_methods(self._state, m)

    def set_download_directory(self, dd):
        tgl.tgl_set_download_directory(self._state, dd)

    def register_app_id(self, id_, hash_):
        tgl.tgl_register_app_id(self._state, id_, hash_)

    def init(self):
        tgl.tgl_init(self._state)

