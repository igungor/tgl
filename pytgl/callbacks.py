from . import ffi, tgl

###################### update callbacks #########################
@ffi.callback("void(struct tgl_state *, struct tgl_message *)")
def _tgl_upd_new_msg_cb(tls, msg):
    pass


@ffi.callback("void(struct tgl_state *, int, struct tgl_message *[])")
def _tgl_upd_marked_read_cb(tls, num, msg_list):
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_user*, enum tgl_typing_status)")
def _tgl_upd_type_notification_cb(tls, user, status):
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_user *, struct tgl_chat*, enum tgl_typing_status)")
def _tgl_upd_type_in_chat_notification_cb(tls, user, chat, status):
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_secret_chat *)")
def _tgl_upd_type_in_secret_chat_notification_cb(tls, chat):
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_user *)")
def _tgl_upd_status_notification_cb(tls, user):
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_user *)")
def _tgl_upd_user_registered_cb(tls, user):
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_user *)")
def _tgl_upd_user_activated_cb(tls, user):
    pass


@ffi.callback("void(struct tgl_state *, const char *, const char*)")
def _tgl_upd_new_authorization_cb(tls, device, location):
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_chat *, unsigned)")
def _tgl_upd_chat_update_cb(tls, chat, flags):
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_chat *, unsigned)")
def _tgl_upd_user_update_cb(tls, chat, flags):
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_secret_chat *, unsigned)")
def _tgl_upd_secret_chat_update_cb(tls, chat, flags):
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_message *")
def _tgl_upd_msg_receive_cb(tls, msg):
    pass


@ffi.callback("void(struct tgl_state *, int)")
def _tgl_upd_our_id_cb(tls, our_id):
    pass


@ffi.callback("void(struct tgl_state *TLS, char *, char *)")
def _tgl_upd_notification_cb(tls, typ, msg):
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_user *)")
def _tgl_upd_user_status_update_cb(tls, user):
    pass


@ffi.callback("char *(struct tgl_state *, tgl_peer_id_t, const char *,const char *,const char *, const char *)")
def _tgl_upd_create_print_name_cb(tls, id_, a1, a2, a3, a4):
    pass



################### net callbacks ######################
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
def _tgl_net_flush_out_cb(conn):
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
def _tgl_net_create_connection_cb(tls, host, port, session, dc, methods):
    pass

################### mtproto callbacks ######################

@ffi.callback("int(struct tgl_state *, struct connection *)")
def _tgl_mtproto_ready_cb(tls, conn):
    pass


@ffi.callback("int(struct tgl_state *, struct connection *)")
def _tgl_mtproto_close_cb(tls, conn):
    pass


@ffi.callback("int(struct tgl_state *, struct connection *, int, int)")
def _tgl_mtproto_execute_cb(tls, conn, op, len_):
    pass


def generate_tgl_update():
    cb = ffi.new('struct tgl_update_callback *')
    cb.new_msg = _tgl_upd_new_msg_cb
    cb.marked_read = _tgl_upd_marked_read_cb
    #cb.logprintf =
    cb.type_notification = _tgl_upd_type_notification_cb
    cb.type_in_chat_notification = _tgl_upd_type_in_chat_notification_cb
    cb.type_in_secret_chat_notification = _tgl_upd_type_in_secret_chat_notification_cb
    cb.status_notification = _tgl_upd_notification_cb
    cb.user_registered = _tgl_upd_user_registered_cb
    cb.user_activated = _tgl_upd_user_activated_cb
    cb.new_authorization = _tgl_upd_new_authorization_cb
    cb.chat_update = _tgl_upd_chat_update_cb
    cb.user_update = _tgl_upd_user_update_cb
    cb.secret_chat_update = _tgl_upd_secret_chat_update_cb
    cb.msg_receive = _tgl_upd_msg_receive_cb
    cb.our_id = _tgl_upd_our_id_cb
    cb.notification = _tgl_upd_notification_cb
    cb.user_status_update = _tgl_upd_user_status_update_cb
    cb.create_print_name = _tgl_upd_create_print_name_cb


def generate_tgl_net():
    cb = ffi.new('struct tgl_net_methods *')
    cb.write_out = _tgl_net_write_out_cb
    cb.read_in = _tgl_net_read_in_cb
    cb.read_in_lookup = _tgl_net_read_in_lookup_cb
    cb.flush_out = _tgl_net_flush_out_cb
    cb.incr_out_packet_num = _tgl_net_incr_out_packet_num_cb
    cb.free = _tgl_net_free_cb
    cb.get_dc = _tgl_net_get_dc_cb
    cb.get_session = _tgl_net_get_session_cb
    cb.create_connection = _tgl_net_create_connection_cb


def generate_tgl_mtproto():
    cb = ffi.new('struct tgl_mtproto_methods *')
    cb.ready = _tgl_mtproto_ready_cb
    cb.close = _tgl_mtproto_close_cb
    cb.execute = _tgl_mtproto_execute_cb



