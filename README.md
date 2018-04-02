# yapiradio

Yet another raspberrypi internet radio is a set of simple scripts that control music playback using a single button, or launching from a Qr code (detected with the pi camera).

It supports local file playback as well as webradios, and is designed for Arch Linux for ARM and tries to minimize dependencies.

## Installing

```
pacman -Sy python-pip gcc zbar libxml2 omxplayer
pip install RPi.GPIO
./install.sh 192.168.1.7
```
