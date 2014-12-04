#/bin/bash
wget https://raw.githubusercontent.com/Shougo/neobundle.vim/master/bin/install.sh -O - | sh  # TODO: md5sum
vim +NeoBundleInstall\(\!\) +qall
 #~/.vim/bundle/neobundle.vim/bin/neoinstall
