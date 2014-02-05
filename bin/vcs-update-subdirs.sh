#!/bin/sh
find $1 -type d -maxdepth 1 | while read d; do cd $d; test -d .git && git pull; cd -; done
