#!/bin/sh
REMOTE_USER=dietpi
TARGET_HOST=192.168.30.15

# Make pycar directory on target host
ssh ${REMOTE_USER}@${TARGET_HOST} 'mkdir ~/pycar'

# Copy contents of pycar directory to pycar/pycar on host
scp -r pycar ${REMOTE_USER}@${TARGET_HOST}:~/pycar/pycar

# Copy requiremets.txt to pycar directory
scp requirements.txt ${REMOTE_USER}@${TARGET_HOST}:~/pycar

# Install python virtualenv
ssh ${REMOTE_USER}@${TARGET_HOST} 'pip3 install virtualenv'

# Make venv directory and create venv
ssh ${REMOTE_USER}@${TARGET_HOST} 'mkdir ~/pycar/venv'
ssh ${REMOTE_USER}@${TARGET_HOST} 'python3 -m virtualenv ~/pycar/venv'

# Source venv and install requirements.txt
ssh ${REMOTE_USER}@${TARGET_HOST} 'source ~/pycar/venv/bin/activate'
ssh ${REMOTE_USER}@${TARGET_HOST} 'pip install -r ~/pycar/requirements.txt'