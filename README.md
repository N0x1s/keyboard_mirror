[![Python 3.9](https://img.shields.io/badge/Python-3.9-green.svg)](http://www.python.org/download/)

# Keyboard mirror

A minimal solution for wanting to use your laptop keyboard with your pc without having a scuffed desk

* no need for Bluetooth
* needs a running x-server


## Tested on

* Arch Linux (tested server and client)
* Windows 10 (tested server and client)
* Mac os (bank balance 8.79$)


## Caution :heavy_multiplication_x:

* You shouldn't use this program, if you don't know what you are doing, it's not aimed towards normal users, this is just a fun (POC) project and probably has many bugs and security issues might remove this warning in the future 

## How to install and use

* install
```shell
# clone repo and cd into it
# pip3 install -U -r requirements.txt
```

* use
```shell
# on the machine that you want to use the keyboard on
python3 server/main.py

# on the machine that you want to share the keyboard off

python3 server/main.py [ip_of_host_machine]
```

```
you can use ctrl+alt+t to switch between sharing the keyboard and not
```

## Todo
* add encryption and authentication
* Support for mouse as well
* fixes some bugs 

I will try to maintain this respiratory and update or add new things to it you are welcome to contribute :relaxed:

And, as always have a beautiful day!
