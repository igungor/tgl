#!/usr/bin/env python

import sys
import os

import pytgl

from pytgl.tgl import TglState
from pytgl.callbacks import *

s = TglState()

s.set_rsa_key(sys.argv[1])

upd_cb = generate_tgl_update()
net_cb = generate_tgl_net()
timer_cb = generate_tgl_timer()
mtproto_cb = generate_tgl_mtproto()

s.set_callback(upd_cb)
s.set_net_methods(net_cb)
s.set_timer_methods(timer_cb)

s.set_download_directory('/tmp')

apphash = "36722c72256a24c1225de00eb6a1ca74"
s.register_app_id(2899, apphash)
s.init()

s.set_auth_file(os.path.expanduser('~/.telegram-cli/auth'))
s.set_state_file(os.path.expanduser('~/.telegram-cli/state'))
s.set_secret_chat_file(os.path.expanduser('~/.telegram-cli/secret'))

s.load_auth()
s.load_secret_chats()
s.load_state()


#read auth state secret
