#!/bin/bash
sudo apt-get install g++
if [[ "$1" == "" ]]; then
    version=3.2.3 # 3.2.5 and 3.2.6 don't work on my xubuntu 
else
    version=$1
fi
An rules of thumb?
ver=mono-$version
filename=$ver.tar.bz2
tmpfolder=/tmp/mono-$version
installfolder=~/3rdparty/$ver
for d in $tmpfolder $installfolder; do
    rm -rf $d; mkdir -p $d
done
wd=`pwd`
cd $tmpfolder

function d() {
    echo `date` $*
    time $*
    exit_code=$?
    echo `date` done with $* - exit code is $? 
}

d wget http://download.mono-project.com/sources/mono/$filename -O $filename
d tar -xjvf $filename
cd $ver
d ./configure --prefix=$installfolder 
d make 
d make install
cd $wd
