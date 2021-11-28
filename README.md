# About

Project for a fully functioning RC car written in Python and controlled by a Dualshock 4 controller


## Prerequisites
1. [Sunfounder PiCar-V](https://www.sunfounder.com/products/smart-video-car)
2. Dualshock 4 controller connected using pyPS4Controller
3. Raspberry Pi, preferably a Pi 4
4. Wifi connection + SSH access

## Initial setup

These steps assume everything under prerequisites has been met.

1. Change `REMOTE_USER` and `TARGET_HOST` vars in `bootstrap.sh`
2. Run `./bootstrap.sh`
3. Enable I2C throug raspi-config
4. Enable raspicam through raspi-config

## Deploying changes

1. Change `REMOTE_USER` and `TARGET_HOST` vars in `deploy.sh`
2. Run `./deploy.sh`
