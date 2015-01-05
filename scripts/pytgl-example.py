#!/usr/bin/env python3

import sys

from pytgl.telegram import Telegram
from pytgl import ffi


def print_message(tls, msg):
    print("new msg: ", ffi.string(msg.message))

@ffi.callback("void(struct tgl_state *, struct tgl_message *)")
def _tgl_upd_new_msg_cb(tls, msg):
    print_message(tls, msg)


@ffi.callback("void(struct tgl_state *, int, struct tgl_message *[])")
def _tgl_upd_marked_read_cb(tls, num, msg_list):
    print("_tgl_upd_marked_read_cb")
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_user*, enum tgl_typing_status)")
def _tgl_upd_type_notification_cb(tls, user, status):
    print("_tgl_upd_type_notification_cb")
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_user *, struct tgl_chat*, enum tgl_typing_status)")
def _tgl_upd_type_in_chat_notification_cb(tls, user, chat, status):
    print("_tgl_upd_type_in_chat_notification_cb")
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_secret_chat *)")
def _tgl_upd_type_in_secret_chat_notification_cb(tls, chat):
    print("_tgl_upd_type_in_secret_chat_notification_cb")
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_user *)")
def _tgl_upd_status_notification_cb(tls, user):
    print("_tgl_upd_status_notification_cb")
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_user *)")
def _tgl_upd_user_registered_cb(tls, user):
    print("_tgl_upd_user_registered_cb")
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_user *)")
def _tgl_upd_user_activated_cb(tls, user):
    print("_tgl_upd_user_activated_cb")
    pass


@ffi.callback("void(struct tgl_state *, const char *, const char*)")
def _tgl_upd_new_authorization_cb(tls, device, location):
    print("_tgl_upd_new_authorization_cb")
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_chat *, unsigned)")
def _tgl_upd_chat_update_cb(tls, chat, flags):
    print("_tgl_upd_chat_update_cb")
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_user *, unsigned)")
def _tgl_upd_user_update_cb(tls, chat, flags):
    print("_tgl_upd_user_update_cb")
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_secret_chat *, unsigned)")
def _tgl_upd_secret_chat_update_cb(tls, chat, flags):
    print("_tgl_upd_secret_chat_update_cb")
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_message *)")
def _tgl_upd_msg_receive_cb(tls, msg):
    print_message(tls, msg)


@ffi.callback("void(struct tgl_state *, int)")
def _tgl_upd_our_id_cb(tls, our_id):
    print("_tgl_upd_our_id_cb")
    pass


@ffi.callback("void(struct tgl_state *TLS, char *, char *)")
def _tgl_upd_notification_cb(tls, typ, msg):
    print("_tgl_upd_notification_cb")
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_user *)")
def _tgl_upd_user_status_update_cb(tls, user):
    print("_tgl_upd_user_status_update_cb")
    pass


def generate_tgl_update():
    from cffi import FFI
    ffi_ = FFI()
    ffi_.cdef("""int printf(const char *format, ...);""")
    C = ffi_.dlopen(None)

    cb = ffi.new('struct tgl_update_callback *')
    cb.new_msg = _tgl_upd_new_msg_cb
    cb.marked_read = _tgl_upd_marked_read_cb
    cb.logprintf = C.printf
    cb.type_notification = _tgl_upd_type_notification_cb
    cb.type_in_chat_notification = _tgl_upd_type_in_chat_notification_cb
    cb.type_in_secret_chat_notification = _tgl_upd_type_in_secret_chat_notification_cb
    cb.status_notification = _tgl_upd_status_notification_cb
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

    #use the default implementation
    #cb.create_print_name = _tgl_upd_create_print_name_cb

    return cb


if len(sys.argv) != 2:
    print("Usage: %s telegram_rsa_key_path" % sys.argv[0])
    sys.exit()

upd_cb = generate_tgl_update()

tg = Telegram(rsa_key = sys.argv[1],
              update_callbacks = upd_cb)

#tg.reset_authorization()
tg.wait_until_authorization()
tg.check_authorization()
print("All DCs are authorized.")

tg.sign_in()
tg.check_sign_in()
print("Signed in.")

tg.store_auth()

tg.send_all_unsent()
print("All unsent msgs are sent.")

tg.get_difference()
print("Entering main loop...")
tg.loop()
