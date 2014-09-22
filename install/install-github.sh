#!/bin/bash
username=$1
reponame=$2
opwd=`pwd`
mkdir -p ~/3rdparty
cd ~/3rdparty
git clone https://github.com/$username/$reponame.git
if [[ -f $reponame/setup.py ]]; then
	cd $reponame
	sudo python setup.py develop
	cd ..
fi
cd $opwd
