#!/bin/bash
tmp_dir=`mktemp -d`
cd $tmp_dir

echo "print __file__" > real.py
ln -s real.py symlink.py
python real.py # prints real.py
python symlink.py # prints symlink.py

cd -
