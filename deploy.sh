#!/bin/sh

export ANSIBLE_HOST_KEY_CHECKING=False
ansible-playbook ansible/deploy.yml -i ${1}, -e 'ansible_python_interpreter=/usr/bin/python3'