#!/bin/bash

function ubuntu-needed-packages() {
    sudo add-apt-repository ppa:relan/exfat
    sudo apt-get update
    sudo apt-get install openssh-server vim git-core cifs-utils exfat-fuse
    git config --global user.name "Peter Zsoldos"
    (git config --global user.email | grep peter\.zsoldos) || (echo "need to setup your git user.email setting! Use git config --global user.email 'someone@somewhere.tld'" && exit 1)
    if [ ! -f ~/.ssh/id_rsa.pub ]; then
        echo "setting up RSA.pub key for github"
        email=`git config --global user.email`
        ssh-keygen -t rsa -C "$email"
    fi 
    echo "Go to https://github.com/settings/ssh to add it github!"
}

ubuntu-needed-packages
dir_name=`pwd`/`dirname $0`
ls -a $dir_name | while read file; do
    if [[ "$file" == '.' ]]; then
       continue
    fi
    if [[ "$file" == '..' ]]; then
       continue
    fi
    if [[ "$file" == '.git' ]]; then
       continue
    fi
    if [[ "$file" == '.gitignore' ]]; then
       continue
    fi
    ln -sf $dir_name/$file ~/
done

function install-python() {
	wget https://raw.github.com/pypa/pip/master/contrib/get-pip.py -O get-pip.py || exit $?
	sudo python get-pip.py || exit $?
    rm get-pip.py
}

install-python || exit $?


function install-github() {
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
}
function install-3rdparty() {
    install-github EnigmaCurry blogofile
    install-github EnigmaCurry blogofile_blog
}


install-3rdparty || exit $?

function vim-pep8() {
    sudo pip install pep8 flake8 || exit $?
    install-github nvie vim-flake8
    for x in ftplugin plugin; do
        mkdir -p ~/.vim/$x/
    done
    find ~/3rdparty/vim-flake8/ftplugin -name \*.vim -type f | while read f; do
        ln -sf $f ~/.vim/ftplugin/
        ln -sf $f ~/.vim/plugin/
    done
}

vim-pep8

source ~/.profile
