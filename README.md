# PiCar
Project for a fully functioning, self-driving PiCar

## Without CV

### Bootstrapping OS

Requirements:
1. Ansible on the machine executing the following steps:

1. Flash OS to SD card 
2. Setup Wifi credentials according to relevant OS settings
3. Change variable `ansible_password` in `ansible/bootstrap/tasks/main.yml` to default user password 
4. Run `bootstrap.sh` <TARGET HOST IP> (e.g. bootstrap.sh 192.168.1.20)

### Deploying PiCar

Requirements:
1. Ansible on the machine executing the following steps:

1. Bootstrap OS
2. Run `deploy.sh` <TARGET HOST IP> (e.g. deploy.sh 192.168.1.20)
   

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


