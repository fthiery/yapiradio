#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2017, Florent Thiery
import time
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO_NB = 14

GPIO.setup(GPIO_NB, GPIO.IN, pull_up_down=GPIO.PUD_UP)

BUTTON_PATH = "/tmp/playlist_index"
PLAYLIST_PATH = "/tmp/uri.txt"


def increment_playlist_index():
    i = 0
    if os.path.isfile(BUTTON_PATH):
        with open(BUTTON_PATH, "r") as f:
            try:
                i = int(f.read())
            except ValueError as e:
                print('Failed to parse int in %s: %s' % (BUTTON_PATH, e))
    with open(BUTTON_PATH, "w") as f:
        i += 1
        print('Playlist incremented to %s' % i)
        f.write(str(i))


def restart_radio():
    print('Restarting radio player')
    os.system('systemctl restart radio.service')


def stop_player():
    print('Stopping music player')
    os.system('systemctl stop player.service')


print('Waiting for button')
while True:
    input_state = GPIO.input(GPIO_NB)
    if input_state != 1:
        print('Button Pressed')
        if not os.path.exists(PLAYLIST_PATH):
            increment_playlist_index()
            restart_radio()
        else:
            # abort player
            stop_player()
            if os.path.exists(PLAYLIST_PATH):
                os.remove(PLAYLIST_PATH)
            restart_radio()
        time.sleep(1)
    time.sleep(0.1)
