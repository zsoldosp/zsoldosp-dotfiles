#!/bin/bash

function ubuntu-needed-packages() {
    sudo apt-get install openssh-server vim git-core
}

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
