#!/bin/bash
readonly PROGDIR=$(readlink -m $(dirname $0))

function ubuntu-needed-packages() {
    cd ansible && ./bootstrap.sh
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
	$PROGDIR/install/install-github.sh $*
}

function install-blogofile() {
    sudo pip install distribute
    install-github EnigmaCurry blogofile
    install-github EnigmaCurry blogofile_blog
}

function install-3rdparty() {
    install-blogofile
}


install-3rdparty || exit $?

$PROGDIR/install/install-vim-flake8.sh

source ~/.profile
