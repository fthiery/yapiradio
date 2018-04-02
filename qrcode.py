#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2017, Florent Thiery
import subprocess
import time
import os

IMG_PATH = "/tmp/qr.jpg"
PLAYER_URI_PATH = "/tmp/uri.txt"


def run_cmd(cmd):
    before = time.time()
    status, output = subprocess.getstatusoutput(cmd)
    took_ms = (time.time() - before)*1000
    print('%s took %ims' % (cmd, took_ms))
    return status == 0, output


def take_picture(img=IMG_PATH):
    raspistill_options = " ".join([
        "-vf -hf -w 640 -h 480 -q 80 -th none -md 7",
        "-ISO 800 --brightness 70 --contrast 70 -ev 10",
        "--nopreview --exposure antishake -t 50"
    ])
    success, output = run_cmd('/opt/vc/bin/raspistill %s -o %s' % (raspistill_options, img))
    return success


def decode_qrcode(img=IMG_PATH):
    success, output = run_cmd('zbarimg -q --raw %s' % img)
    if success:
        return output


print('Started')
while True:
    if not os.path.exists(PLAYER_URI_PATH):
        start = time.time()
        if take_picture():
            uri = decode_qrcode()
            if uri:
                print('Found qrcode containing %s' % uri)
                uri = "/root/music/L'ours qui ne rentrait plus dans son slip"
                with open(PLAYER_URI_PATH, 'w') as f:
                    f.write(uri)
                subprocess.getoutput('systemctl stop radio.service')
                subprocess.getoutput('systemctl start player.service')
        print('Took %ims' % (1000*(time.time() - start)))
    else:
        time.sleep(1)
