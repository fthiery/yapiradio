#!/bin/bash
# Copyright 2017, Florent Thiery
if [ $# -eq 0 ]
  then
    echo "No arguments supplied; usage: ./install.sh 192.168.1.7"
  else
    ssh root@$1 writeenable.sh
    scp *.py root@$1:/root
    scp playlist.m3u8 root@$1:/root
    scp *.service root@$1:/usr/lib/systemd/system/
    ssh root@$1 systemctl daemon-reload
    ssh root@$1 systemctl enable radio.service
    ssh root@$1 systemctl enable radio-button.service
    ssh root@$1 systemctl enable qrcode.service
fi
