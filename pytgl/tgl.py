from . import ffi, tgl

def _tgl_new_msg_cb():
    pass

def _tgl_marked_read_cb():
    pass

@ffi.callback("int(struct connection *, const void *, int)")
def _tgl_net_write_out_cb(conn, data, len_):
    pass


@ffi.callback("int(struct connection *, const void *, int)")
def _tgl_net_read_in_cb(conn, data, len_):
    pass


@ffi.callback("int(struct connection *, const void *, int)")
def _tgl_net_read_in_lookup_cb(conn, data, len_):
    pass


@ffi.callback("void(struct connection *)")
def _tgl_net_flash_out_cb(conn):
    pass


@ffi.callback("void(struct connection *)")
def _tgl_net_incr_out_packet_num_cb(conn):
    pass


@ffi.callback("void(struct connection *)")
def _tgl_net_free_cb(conn):
    pass

@ffi.callback("struct tgl_dc *(struct connection *)")
def _tgl_net_get_dc_cb(conn):
    pass


@ffi.callback("struct tgl_session *(struct connection *)")
def _tgl_net_get_session_cb(conn):
    pass


@ffi.callback("struct connection *(struct tgl_state *, const char *, int, struct tgl_session *, struct tgl_dc *, struct mtproto_methods *)")
def _tgl_net_create_connection_cb(tls, host, port, session, dc. methods):
    pass


@ffi.callback("int(struct tgl_state *, struct connection *)")
def _tgl_mtproto_ready_cb(tls, conn):
    pass


@ffi.callback("int(struct tgl_state *, struct connection *)")
def _tgl_mtproto_close_cb(tls, conn):
    pass


@ffi.callback("int(struct tgl_state *, struct connection *, int, int)")
def _tgl_mtproto_execute_cb(tls, conn, op, len_):
    pass


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


