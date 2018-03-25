# yapiradio

Yet another raspberrypi internet radio is a set of simple scripts that control music playback using a single button. It supports local file playback as well as webradios, and is designed for Arch Linux for ARM and tries to minimize dependencies.

## Installing

```
pacman -Sy mpg123 python-pip gcc
pip install RPi.GPIO
./install.sh 192.168.1.7
```
