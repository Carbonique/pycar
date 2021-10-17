#!/bin/sh
REMOTE_USER=dietpi
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

# Install python3 and pip
echo "Installing python3 and pip"
echo
ssh ${REMOTE_USER}@${TARGET_HOST} 'sudo apt-get install python-dev python3 pip -y'
echo
echo "python3 and pip installed"

# Install virtualenv
echo "Installing virtualenv"
echo
ssh ${REMOTE_USER}@${TARGET_HOST} 'pip3 install virtualenv'
echo
echo "Virtualenv installed"