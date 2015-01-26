#!/bin/bash
if [[ $(which ansible) == "" ]]; then
	sudo apt-get install software-properties-common
	sudo apt-add-repository ppa:ansible/ansible
	sudo apt-get update
	sudo apt-get install ansible
fi
ansible localhost -m ping
sudo ansible-playbook general.yml 
