#!/bin/bash

function ubuntu-needed-packages() {
    sudo apt-get install openssh-server vim git-core
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

function vim-pep8() {
    sudo pip install pep8 flake8
    git clone https://github.com/nvie/vim-flake8.git ~/vim-flake8
    mkdir -p ~/.vim/plugin
    find ~/vim-flake8/ftplugin -name \*.vim -type f | while read f; do
        ln -sf $f ~/.vim/ftplugin/
        ln -sf $f ~/.vim/plugin/
    done
}

vim-pep8

source ~/.profile
