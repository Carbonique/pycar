# pycar
Project for a fully functioning, self-driving pycar

## Without CV

### Bootstrapping OS

Requirements:
1. Ansible on the machine executing the following steps:

1. Flash DietPi to SD card 
2. Setup Wifi credentials according to DietPi requirements
3. Install Python on DietPi: `sudo apt-get install python3 -y`
4. Change variable `ansible_password` in `ansible/bootstrap/tasks/main.yml` to default user password 
5. Run `./bootstrap.sh` <TARGET HOST IP> (e.g. bootstrap.sh 192.168.1.20)
6. Enable I2C throug dietpi-config

### Deploying pycar

Requirements:
1. Ansible on the machine executing the following steps:

1. Bootstrap DietPi (see instructions above)
2. Run `./deploy.sh` <TARGET HOST IP> (e.g. deploy.sh 192.168.1.20)
   

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


