#!/usr/bin/env python

import sys
import os

from pytgl.telegram import Telegram
from pytgl.callbacks import *

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
tg.load_secret_chats()
tg.load_state()
