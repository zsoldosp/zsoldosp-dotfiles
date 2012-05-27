#!/bin/bash
sudo mount /dev/cdrom1 /media/cdrom
cp /media/cdrom/VMwareTools-*.tar.gz /tmp/ || (echo "need to make the vmware tools cd available to the VM" && exit 1)
sudo umount /media/cdrom/
cd /tmp
tar xzvf VMwareTools-*.tar.gz
cd vmware-tools-distrib/
kernel_version=`uname -a | cut -f 3 -d ' '`
headers_to_install=`apt-cache search  header | grep "^linux-headers-$kernel_version" | cut -f 1 -d ' '`
sudo aptitude install build-essential gcc binutils make $headers_to_install
sudo ./vmware-install.pl -d
sudo /etc/init.d/networking stop
sudo rmmod pcnet32
sudo rmmod vmxnet
sudo modprobe vmxnet
sudo /etc/init.d/networking start
