from . import ffi, tgl

from .callbacks import *

class Telegram(object):
    def __init__(self,
                 rsa_key,
                 download_dir,
                 update_callbacks,
                 app_id,
                 app_hash):

        self._state = ffi.new('struct tgl_state *')
        self._download_dir = download_dir

        #files
        self._auth_file = None
        self._secret_chat_file = None
        self._state_file = None

        self._app_id = app_id
        self._app_hash = app_hash
        self._rsa_keypath = rsa_key

        self.set_callback(update_callbacks)
        tgl.tgln_set_evbase(self._state)

        self.set_net_methods(ffi.addressof(tgl.tgl_conn_methods))
        self.set_timer_methods(ffi.addressof(tgl.tgl_libevent_timers))
        self.set_serialize_methods(ffi.addressof(tgl.tgl_file_methods))

        self.set_rsa_key(self._rsa_keypath)

        self.set_download_directory(self._download_dir)

        self.register_app_id(self._app_id, self._app_hash)

        tgl.tgl_init(self._state)

    def set_callback(self, cb):
        tgl.tgl_set_callback(self._state, cb)

    def set_net_methods(self, m):
        self._state.net_methods = m

    def set_timer_methods(self, m):
        self._state.timer_methods = m

    def set_serialize_methods(self, m):
        self._state.serialize_methods = m

    def set_download_directory(self, dd):
        self._download_dir = dd
        tgl.tgl_set_download_directory(self._state, self._download_dir)

    def set_auth_file(self, path):
        self._auth_file = path
        tgl.tgl_set_auth_file_path(self._state, self._auth_file)

    def set_secret_chat_file(self, path):
        self._secret_chat_file = path
        tgl.tgl_set_secret_chat_file_path(self._state, self._secret_chat_file)

    def set_state_file(self, path):
        self._state_file = path
        tgl.tgl_set_state_file_path(self._state, self._state_file)

    def set_rsa_key(self, keypath):
        self._rsa_keypath = keypath
        tgl.tgl_set_rsa_key(self._state, self._rsa_keypath)

    def register_app_id(self, id_, hash_):
        self._appid = id_
        self._apphash = hash_

        tgl.tgl_register_app_id(self._state, self._appid, self._apphash)

    def load_auth(self):
        self._state.serialize_methods.load_auth(self._state)

    def load_state(self):
        self._state.serialize_methods.load_state(self._state)

    def load_secret_chats(self):
        self._state.serialize_methods.load_secret_chats(self._state)

    def loop(self, flags = 0, is_end = None):
        if is_end is None:
            cb = ffi.NULL
        else:
            cb = ffi.callback("int (*)(void)", is_end)

        tgl.wait_for_event(self._state, flags, cb)

    def all_authorized(self):
        s = self._state
        max_dc = s.max_dc_num
        return all([tgl.tgl_authorized_dc(s, s.DC_list[i])
                   for i in range(1, max_dc+1)]) #WTF!!!

