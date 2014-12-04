set termencoding=utf-8
set fileencoding=utf-8
set encoding=utf-8
set ignorecase
set smartcase
set number

let g:flake8_max_line_length=120

function ZspTabsAsSpaces()
    setlocal tabstop=4
    setlocal shiftwidth=4
    setlocal smarttab
    setlocal expandtab
    setlocal softtabstop=4
endfunction

if !exists("autocommands_loaded")
    let autocommands_loaded = 1
    autocmd FileType python call ZspTabsAsSpaces()
endif

"NeoBundle Scripts-----------------------------
if has('vim_starting')
  set nocompatible               " Be iMproved

  " Required:
  set runtimepath+=/home/peter/.vim/bundle/neobundle.vim/
  " TODO: this above needs to be made relative path somehow
endif

" Required:
call neobundle#begin(expand('/home/peter/.vim/bundle'))

" Let NeoBundle manage NeoBundle
" Required:
NeoBundleFetch 'Shougo/neobundle.vim'

" Add or remove your Bundles here:
NeoBundle 'Shougo/neosnippet.vim'
NeoBundle 'Shougo/neosnippet-snippets'
NeoBundle 'tpope/vim-fugitive'
NeoBundle 'ctrlpvim/ctrlp.vim'
NeoBundle 'flazz/vim-colorschemes'
NeoBundle 'flazz/vim-colorschemes'
NeoBundle 'dhruvasagar/vim-table-mode'

" You can specify revision/branch/tag.
NeoBundle 'Shougo/vimshell', { 'rev' : '3787e5' }

" Required:
call neobundle#end()

" Required:
filetype plugin indent on

" If there are uninstalled bundles found on startup,
" this will conveniently prompt you to install them.
NeoBundleCheck
"End NeoBundle Scripts-------------------------

