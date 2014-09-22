#!/bin/bash
readonly PROGDIR=$(readlink -m $(dirname $0))
sudo pip install pep8 flake8 || exit $?
$PROGDIR/install-github.sh nvie vim-flake8
for x in ftplugin plugin; do
	mkdir -p ~/.vim/$x/
done
find ~/3rdparty/vim-flake8/ftplugin -name \*.vim -type f | while read f; do
	ln -sf $f ~/.vim/ftplugin/
	ln -sf $f ~/.vim/plugin/
done

