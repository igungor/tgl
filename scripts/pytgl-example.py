#!/usr/bin/env python3

import sys

from pytgl.telegram import Telegram
from pytgl import ffi
from pytgl.callbacks import generate_tgl_update


@ffi.callback("void(struct tgl_state *, struct tgl_message *)")
def _msg_cb(tls, msg):
    print("New message: ", ffi.string(msg.message).decode())


if len(sys.argv) != 2:
    print("Usage: %s telegram_rsa_key_path" % sys.argv[0])
    sys.exit()


upd_cb = generate_tgl_update()
upd_cb.new_msg = _msg_cb
upd_cb.msg_receive = _msg_cb


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
