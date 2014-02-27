set termencoding=utf-8
set fileencoding=utf-8
set encoding=utf-8
set ignorecase
set smartcase
set number

function ZspTabsAsSpaces()
    setlocal tabstop=4
    setlocal shiftwidth=4
    setlocal smarttab
    setlocal expandtab
    setlocal softtabstop=4
endfunction

if !exists("autocommands_loaded")
    let autocommands_loaded = 1
    autocmd FileType python call ZspTabsAsSpaces
endif
