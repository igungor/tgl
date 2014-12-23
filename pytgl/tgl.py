from . import ffi, tgl


class TglState(object):
    def __init__(self):
        self._state = ffi.new('tgl_state *')
        self._update_cb = ffi.new('tgl_update_callback *')

    def set_callback(self, cb):
        tgl.tgl_set_callback(self._state, cb)

    def set_net_methods(self, m):
        tgl.tgl_set_new_methods(self._state, m)

    def init(self):
        tgl.tgl_init(self._state)

