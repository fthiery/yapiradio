#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright 2017, Florent Thiery
# deps: python mpg123

import time
import os


BUTTON_PATH = "/tmp/playlist_index"
PLAYLIST_PATH = "/root/playlist.m3u8"


def test_connection():
    url = "http://www.google.com"
    return os.system('curl -I %s &> /dev/null' % url) == 0


def wait_for_connection():
    while not test_connection():
        print('No connection, sleeping 500ms')
        time.sleep(0.5)


def get_playlist():
    playlist = list()
    with open(PLAYLIST_PATH, 'r') as f:
        lines = f.read().strip().split('\n')
    for l in lines:
        if not l.startswith('#'):
            playlist.append(l)
    return playlist


def get_playlist_index():
    if os.path.isfile(BUTTON_PATH):
        with open(BUTTON_PATH, 'r') as f:
            try:
                return int(f.read())
            except Exception as e:
                print('Malformed %s file, ignoring: %s' % (BUTTON_PATH, e))


def play():
    try:
        playlist = get_playlist()
    except Exception as e:
        print('Failed to parse playlist %s, falling back to default playlist' % PLAYLIST_PATH)
        playlist = ["http://api.radiopommedapi.com/radio.mp3"]

    playlist_index = get_playlist_index()
    if playlist_index is None:
        playlist_index = 0
    playlist_index = playlist_index % len(playlist)
    url = playlist[playlist_index]
    print("Opening playlist item nb %s/%s: %s" % (playlist_index, len(playlist), url))
    os.system('mpg123 %s' % url)


def start_radio():
    while True:
        play()
        print('mpg123 exited, sleeping 1s')
        time.sleep(1)


wait_for_connection()
start_radio()
