# pIRemote
IR universal remote using a Raspberry Pi - connect that to a Google Home or Amazon Alexa and you're good to go!

It's more of a gist as of now, but I'll automate the process where possible.

# Hardware Requirements 
IR emitter and receiver(s): https://amzn.to/2InADWe

# Hardware Setup

GPIO Pinout reference: https://pinout.xyz/

# Software Setup
Install lirc: `sudo apt-get install lirc`
Add the following to your `/etc/modules`:
```
lirc_dev
lirc_rpi gpio_in_pin=18 gpio_out_pin=17
```
Remember to change `gpio_in_pin` and `gpio_out_pin` according to your hardware setup

Put the following in `/etc/lirc/hardware.conf`:
```
LIRCD_ARGS="--uinput"
# Try to load appropriate kernel modules
LOAD_MODULES=true
# Run "lircd --driver=help" for a list of supported drivers.
DRIVER="default"
# usually /dev/lirc0 is the correct setting for systems using udev
DEVICE="/dev/lirc0"
MODULES="lirc_rpi"
# Default configuration files for your hardware if any
LIRCD_CONF=""
LIRCMD_CONF=""
```
Add the following to your `/boot/config.txt`:
```
dtoverlay=gpio-ir-tx,gpio_pin=17
dtoverlay=gpio-ir,gpio_pin=18
```

create your `/etc/systemd/system/piremote.service` like so:
```
[Unit]
Description=Pi remote service
After=network.target 

[Service]
Type=idle
User=pi
Group=pi
EnvironmentFile=/home/pi/.profile
ExecStart=/bin/bash -l -c '/home/pi/piremote.py'
ExecReload=/bin/kill -HUP $MAINPID
KillMode=control-group

[Install]
WantedBy=multi-user.target
```
and of course, copy/move `piremote.py` to your home folder: 

`cp piremote.py /home/pi/piremote.py`

# Initial Configuration:

## To record a button from a remote:
`ir-ctl --device=/dev/lirc1 --record=button.txt`

remember to change `/dev/lirc1` with your actual receiver 

(could also be lirc0 - check with `ir-ctl --device=/dev/lirc1 --features`)

## To send a button:
`ir-ctl --send=button.txt`


