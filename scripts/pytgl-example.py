#!/usr/bin/env python

import sys
import os

from pytgl.telegram import Telegram, tgl
from pytgl import ffi


def print_message(tls, msg):
    print "new msg: ", ffi.string(msg.message)

@ffi.callback("void(struct tgl_state *, struct tgl_message *)")
def _tgl_upd_new_msg_cb(tls, msg):
    print_message(tls, msg)


@ffi.callback("void(struct tgl_state *, int, struct tgl_message *[])")
def _tgl_upd_marked_read_cb(tls, num, msg_list):
    print "_tgl_upd_marked_read_cb"
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_user*, enum tgl_typing_status)")
def _tgl_upd_type_notification_cb(tls, user, status):
    print "_tgl_upd_type_notification_cb"
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_user *, struct tgl_chat*, enum tgl_typing_status)")
def _tgl_upd_type_in_chat_notification_cb(tls, user, chat, status):
    print "_tgl_upd_type_in_chat_notification_cb"
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_secret_chat *)")
def _tgl_upd_type_in_secret_chat_notification_cb(tls, chat):
    print "_tgl_upd_type_in_secret_chat_notification_cb"
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_user *)")
def _tgl_upd_status_notification_cb(tls, user):
    print "_tgl_upd_status_notification_cb"
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_user *)")
def _tgl_upd_user_registered_cb(tls, user):
    print "_tgl_upd_user_registered_cb"
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_user *)")
def _tgl_upd_user_activated_cb(tls, user):
    print "_tgl_upd_user_activated_cb"
    pass


@ffi.callback("void(struct tgl_state *, const char *, const char*)")
def _tgl_upd_new_authorization_cb(tls, device, location):
    print "_tgl_upd_new_authorization_cb"
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_chat *, unsigned)")
def _tgl_upd_chat_update_cb(tls, chat, flags):
    print "_tgl_upd_chat_update_cb"
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_user *, unsigned)")
def _tgl_upd_user_update_cb(tls, chat, flags):
    print "_tgl_upd_user_update_cb"
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_secret_chat *, unsigned)")
def _tgl_upd_secret_chat_update_cb(tls, chat, flags):
    print "_tgl_upd_secret_chat_update_cb"
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_message *)")
def _tgl_upd_msg_receive_cb(tls, msg):
    print_message(tls, msg)


@ffi.callback("void(struct tgl_state *, int)")
def _tgl_upd_our_id_cb(tls, our_id):
    print "_tgl_upd_our_id_cb"
    pass


@ffi.callback("void(struct tgl_state *TLS, char *, char *)")
def _tgl_upd_notification_cb(tls, typ, msg):
    print "_tgl_upd_notification_cb"
    pass


@ffi.callback("void(struct tgl_state *, struct tgl_user *)")
def _tgl_upd_user_status_update_cb(tls, user):
    print "_tgl_upd_user_status_update_cb"
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
    print "Usage: %s telegram_rsa_key_path" % sys.argv[0]
    sys.exit()

upd_cb = generate_tgl_update()

tg = Telegram(rsa_key = sys.argv[1],
              download_dir = '/tmp',
              update_callbacks = upd_cb,
              app_id = 2899,
              app_hash = "36722c72256a24c1225de00eb6a1ca74")

tg.set_auth_file(os.path.expanduser('~/.telegram-cli/auth'))
tg.set_state_file(os.path.expanduser('~/.telegram-cli/state'))
tg.set_secret_chat_file(os.path.expanduser('~/.telegram-cli/secret'))

tg.load_auth()
tg.load_state()
tg.load_secret_chats()

#tgl.bl_do_reset_authorization(tg._state)

tg.loop(0, lambda: int(tg.all_authorized()))
print "All DCs are authorized."

for i in range(1, tg._state.max_dc_num+1):
    if tg._state.DC_list[i] and not tgl.tgl_authorized_dc(tg._state, tg._state.DC_list[i]):
        assert False

if not tgl.tgl_signed_dc (tg._state, tg._state.DC_working):
    username = raw_input("Telephone number (with '+' sign): ")

    registered = False
    hash_ = None

    @ffi.callback("void (*)(struct tgl_state *, void *, int , int , const char *)")
    def sign_in_cb(tls, extra, success, registeredarg, mhasharg):
        global registered
        global hash_

        if success:
            registered = registeredarg
            hash_ = mhasharg

    tgl.tgl_do_send_code (tg._state, username, sign_in_cb, ffi.NULL);
    tg.loop(0, lambda: hash_ is not None)

    if registered:
        print 'Code from SMS (if you did not receive an SMS and want' \
              ' to be called, type "call"): ',

        while True:
            code = raw_input()
            if code.strip() == 'call':
                tgl.tgl_do_phone_call (tg._state, username, hash_, ffi.NULL, ffi.NULL);
                print "Code: ",
                continue

            signed_in = False
            @ffi.callback('void (*)(struct tgl_state *TLSR, void *extra, int' \
                          ' success, struct tgl_user *U)')
            def sign_in_result_cb(tls, extra, success, user):
                global signed_in
                if success:
                    signed_in = True

            if tgl.tgl_do_send_code_result(tg._state, username, hash_, code,
                    sign_in_result_cb, ffi.NULL) >= 0:
                break
            print "Invalid code. Try again: ",

    else:
        print "Registeration is not implemented yet..."
        sys.exit(0)

for i in range(1, tg._state.max_dc_num+1):
    if tg._state.DC_list[i] and not tgl.tgl_signed_dc(tg._state, tg._state.DC_list[i]):
        tgl.tgl_do_export_auth(tg._state, i-1, ffi.NULL, tg._state.DC_list[i])
        tg.loop(0, lambda: tgl.tgl_signed_dc(tg._state, tg._state.DC_list[i]))
        assert tgl.tgl_signed_dc(tg._state, tg._state.DC_list[i])

tg.store_auth()

tgl.tglm_send_all_unsent(tg._state)
print "All unsent msgs are sent."

diff_success = 0
@ffi.callback("void (*)(struct tgl_state *, void *, int)")
def get_diff_cb(tls, extra, success):
    global diff_success
    if success:
        diff_success = 1


tgl.tgl_do_get_difference(tg._state, 0, get_diff_cb, ffi.NULL)

tg.loop(0, lambda: diff_success)
print "Got difference."

tg._state.started = 1

print "Entering main loop..."
tg.loop()
