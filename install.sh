#!/bin/bash

function ubuntu-needed-packages() {
    sudo apt-get install openssh-server vim git-core
    git config --global user.name "Peter Zsoldos"
    (git config --global user.email | grep peter\.zsoldos) || echo "need to setup your git user.email setting! Use git config --global user.email 'someone@somewhere.tld'"

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
    ln -sf $dir_name/$file ~/
done
