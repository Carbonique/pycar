# pycar
Project for a fully functioning, self-driving pycar

## Without CV

### Bootstrapping OS

Requirements:
1. Ansible on the machine executing the following steps:

1. Flash RP OS lite to SD card 
2. Setup Wifi credentials according to requirements
3. Change `RERMOTE_USER` and `TARGET_HOST` vars in `bootstrap.sh`
4. Run `./bootstrap.sh`
5. Enable I2C throug raspi-config

### Deploying pycar

Requirements:
1. Bootstrap DietPi (see instructions above)

1. Change `RERMOTE_USER` and `TARGET_HOST` vars in `deploy.sh`
2. Run `./deploy.sh` 
   

## With CV

1. Download OS from: https://github.com/google-coral/edgetpu-platforms and burn to SD
2. Add wifi credentials to sd card (wpa_supplicant.conf)
   ```
    country=NL
    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    network={
        ssid="MyWiFiNetwork"
        psk="aVeryStrongPassword"
        key_mgmt=WPA-PSK
    }
   ```
3. Optional: assign static IP
4. Change password
5. Expand filesystem


