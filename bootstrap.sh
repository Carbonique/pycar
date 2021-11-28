#!/bin/sh
REMOTE_USER=pi
TARGET_HOST=192.168.30.15

# Copy SSH key to target host

echo "Copying SSH key to target host"
echo
ssh-copy-id ${REMOTE_USER}@${TARGET_HOST}
echo
echo "Done copying"

# Change password
echo "Changing password"
echo
ssh ${REMOTE_USER}@${TARGET_HOST} 'passwd'
echo
echo "Password changed"

# Disable root login over ssh
echo "Disabling root login over ssh"
echo
ssh ${REMOTE_USER}@${TARGET_HOST} "sudo sed -i 's/PermitRootLogin yes/PermitRootLogin no/g' /etc/ssh/sshd_config"
echo
echo "Root login disabled"

# Disable SSH password login
echo "Disabling ssh password login"
echo
ssh ${REMOTE_USER}@${TARGET_HOST} "sudo sed -E -i 's|^#?(PasswordAuthentication)\s.*|\1 no|' /etc/ssh/sshd_config"
echo
echo "Password login disabled"

echo "Restarting ssh"
echo
ssh ${REMOTE_USER}@${TARGET_HOST} 'sudo systemctl restart ssh'
echo
echo "ssh restarted"

echo "Updating and installing pip"
echo
ssh ${REMOTE_USER}@${TARGET_HOST} 'sudo apt-get update && sudo apt-get upgrade -y'
ssh ${REMOTE_USER}@${TARGET_HOST} 'sudo apt-get install python3-pip -y'
echo
echo "Install succesful"

# Install virtualenv
echo "Installing virtualenv"
echo
ssh ${REMOTE_USER}@${TARGET_HOST} 'pip3 install virtualenv'
echo
echo "Virtualenv installed"

# Make venv directory and create venv
ssh ${REMOTE_USER}@${TARGET_HOST} 'mkdir ~/pycar'
ssh ${REMOTE_USER}@${TARGET_HOST} 'mkdir ~/pycar/venv'
ssh ${REMOTE_USER}@${TARGET_HOST} 'python3 -m virtualenv ~/pycar/venv'
