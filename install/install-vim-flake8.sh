#!/bin/bash
readonly PROGDIR=$(readlink -m $(dirname $0))
sudo pip install pep8 flake8 || exit $?
$PROGDIR/install-github.sh nvie vim-flake8

find ~/3rdparty/vim-flake8/  -mindepth 1 -maxdepth 1 -type d ! -name .git | while read d; do
	d_name=$(basename $d)
	trg=~/.vim/$d_name
	test -d $trg || mkdir -p $trg
	find $d -name \*.vim -type f | while read f; do
		src_f=$f
		trg_f=$trg/$(basename $f)
		ln -sf $src_f $trg_f
	done
done
ln -sf ~/.vim/ftplugin ~/.vim/plugin
