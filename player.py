#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2017, Florent Thiery

import os
import shlex

PLAYER_URI_PATH = "/tmp/uri.txt"


def scan_folder(path):
    cmds = []
    files = os.listdir(path)
    files.sort()
    for f in files:
        abspath = os.path.join(path, f)
        cmds.append("omxplayer --vol -2000 %s" % shlex.quote(abspath))
    return cmds


with open(PLAYER_URI_PATH, 'r') as f:
    path = f.read().strip()
    print(path)

if os.path.exists(path):
    commands = scan_folder(path)
    for c in commands:
        print(c)
        os.system(c)
    if os.path.exists(PLAYER_URI_PATH):
        os.remove(PLAYER_URI_PATH)
    os.system("systemctl start radio.service")
