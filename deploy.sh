#!/bin/sh
REMOTE_USER=pi
TARGET_HOST=192.168.30.15

# Copy contents of pycar directory to pycar/pycar on host
rsync -avzh pycar/ ${REMOTE_USER}@${TARGET_HOST}:~/pycar/pycar --delete

# Copy requiremets.txt to pycar directory
scp requirements.txt ${REMOTE_USER}@${TARGET_HOST}:~/pycar

# Source venv and install requirements.txt

#ssh ${REMOTE_USER}@${TARGET_HOST} 'source ~/pycar/venv/bin/activate'
#ssh ${REMOTE_USER}@${TARGET_HOST} 'pip3 install -r ~/pycar/requirements.txt'
