from . import ffi, tgl

from .callbacks import *

class TglState(object):
    def __init__(self):
        self._state = ffi.new('struct tgl_state *')
        self._update_cb = ffi.new('struct tgl_update_callback *')
        self._download_dir = None
        self._appid = -1
        self._apphash = None
        self._rsa_keypath = None

    def set_callback(self, cb):
        tgl.tgl_set_callback(self._state, cb)

    def set_net_methods(self, m):
        self._state.net_methods = m

    def set_timer_methods(self, m):
        self._state.timer_methods = m

    def set_download_directory(self, dd):
        self._download_dir = dd
        tgl.tgl_set_download_directory(self._state, self._download_dir)

    def set_rsa_key(self, keypath):
        self._rsa_keypath = keypath
        tgl.tgl_set_rsa_key(self._state, self._rsa_keypath)

    def register_app_id(self, id_, hash_):
        self._appid = id_
        self._apphash = hash_

        tgl.tgl_register_app_id(self._state, self._appid, self._apphash)

    def init(self):
        tgl.tgl_init(self._state)

