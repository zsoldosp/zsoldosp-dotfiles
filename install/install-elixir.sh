#!/bin/bash
function install-esl-erlang-if-needed() {
    # install esl-erlang a'la http://devblog.avdi.org/2013/07/05/installing-elixir-on-ubuntu-13-04/
    sources_file=/etc/apt/sources.list
    line="deb http://binaries.erlang-solutions.com/debian raring contrib"
    grep "$line" $sources_file > /dev/null 
    if [[ "$?" != 0 ]]; then
        echo "$line" | sudo tee -a $sources_file
        sudo apt-get update && sudo apt-get install esl-erlang
    fi
}

function install-elixir-release() {
    version=$1
    owd=`pwd`
    cd ~/3rdparty
    # from http://elixir-lang.org/getting_started/1.html
    f=elixir-${version}
    wget https://github.com/elixir-lang/elixir/archive/v${version}.tar.gz -O $f.tar.gz
    rm -rf $f || exit $?
    tar -zxvf $f.tar.gz || exit $?
    cd $f
    make
    cd ..
    rm elixir || true
    ln -s $f elixir
    cd $owd
}

function install-elixir-master() {
    owd=`pwd`
    cd ~/3rdparty
    # from http://elixir-lang.org/getting_started/1.html
    f=elixir-master
    if [ -d $f ]; then
        cd $f
        git pull 
        cd -
    else
        git clone https://github.com/elixir-lang/elixir/ $f
    fi
    cd $f
    make
    cd ..
    rm elixir || true
    ln -s $f elixir
    cd $owd
}

function install-elixir() {
    if [[ "$1" == "" ]]; then
        install-elixir-master $*
    else
        install-elixir $*
    fi
}

install-esl-erlang-if-needed && install-elixir $*
