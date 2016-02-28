" Use Vim settings, rather then Vi settings (much better!).
" This must be first, because it changes other options as a side effect.
set nocompatible


filetype off
call pathogen#incubate()
call pathogen#helptags()
let g:syntastic_php_checkers = ['phpcs']
let g:syntastic_php_phpcs_args=" --standard=Drupal --extensions=php,module,inc,install,test,profile,theme"
if has('statusline')
  set laststatus=2
  " Broken down into easily includeable segments
  set statusline=%<%f\ " Filename
  set statusline+=%w%h%m%r " Options
  set statusline+=%{fugitive#statusline()} " Git Hotness
"  set statusline+=\ [%{&ff}/%Y] " filetype
"  set statusline+=\ [%{getcwd()}] " current dir
"  set statusline+=%#warningmsg#
  set statusline+=%{SyntasticStatuslineFlag()}
  set statusline+=%*
  let g:syntastic_enable_signs=1
  set statusline+=%=%-14.(%l,%c%V%)\ %p%% " Right aligned file nav info
endif
" execute pathogen#infect()

au BufNewFile,BufRead *.less set filetype=less

" Map a mode for preserving indent when pasting
nnoremap <F8> :set invpaste paste?<CR>
set pastetoggle=<F8>
set showmode


autocmd ColorScheme * highlight ExtraWhitespace ctermbg=red guibg=red
highlight ExtraWhitespace ctermbg=red guibg=red
match ExtraWhitespace /\s\+$/
"set showmatch
set shiftwidth=2
set ts=2
set expandtab
set autoindent
set smartindent

" allow backspacing over everything in insert mode
set backspace=indent,eol,start

"if has("vms")
"  set nobackup		" do not keep a backup file, use versions instead
"else
"  set backup		" keep a backup file
"endif
set history=50000		" keep 50 lines of command line history
set ruler		" show the cursor position all the time
set showcmd		" display incomplete commands
"set incsearch		" do incremental searching

" Don't use Ex mode, use Q for formatting
map Q gq

" CTRL-U in insert mode deletes a lot.  Use CTRL-G u to first break undo,
" so that you can undo CTRL-U after inserting a line break.
inoremap <C-U> <C-G>u<C-U>

" In many terminal emulators the mouse works just fine, thus enable it.
if has('mouse')
  set mouse=a
endif

" This is an alternative that also works in block mode, but the deleted
" text is lost and it only works for putting the current register.
"vnoremap p "_dp

" Switch syntax highlighting on, when the terminal has colors
" Also switch on highlighting the last used search pattern.
if &t_Co > 2 || has("gui_running")
  syntax on
  set hlsearch
endif


if has("autocmd")
" Only do this part when compiled with support for autocommands.
  augroup module
    autocmd BufRead,BufNewFile *.test set filetype=php
    autocmd BufRead,BufNewFile *.module set filetype=php
    autocmd BufRead,BufNewFile *.install set filetype=php
  augroup END

  " Enable file type detection.
  " Use the default filetype settings, so that mail gets 'tw' set to 72,
  " 'cindent' is on in C files, etc.
  " Also load indent files, to automatically do language-dependent indenting.
  filetype plugin indent on

  " Put these in an autocmd group, so that we can delete them easily.
  augroup vimrcEx
  au!

  " For all text files set 'textwidth' to 78 characters.
"  autocmd FileType text setlocal textwidth=78

  " When editing a file, always jump to the last known cursor position.
  " Don't do it when the position is invalid or when inside an event handler
  " (happens when dropping a file on gvim).
"  autocmd BufReadPost *
"    \ if line("'\"") > 0 && line("'\"") <= line("$") |
"    \   exe "normal g`\"" |
"    \ endif

  autocmd BufReadPost *
    \ if line("'\"") > 1 && line("'\"") <= line("$") |
    \   exe "normal! g`\"" |
    \ endif

  augroup END

else


endif " has("autocmd")

function! ResCur()
  if line("'\"") <= line("$")
    normal! g`"
    return 1
  endif
endfunction

augroup resCur
  autocmd!
  autocmd BufWinEnter * call ResCur()
augroup END

autocmd FileType php map <F5> <ESC>:EnableFastPHPFolds<Cr>
autocmd FileType php map <F6> <ESC>:EnablePHPFolds<Cr>
autocmd FileType php map <F7> <ESC>:DisablePHPFolds<Cr>

autocmd FileType python map <F5> <ESC>:w<CR>:!python %<CR>
autocmd FileType python map <F6> :s/^/#/<CR>/&^<CR>
autocmd FileType python map <F7> :s/^#//<CR>/&^<CR>

" Tell vim to remember certain things when we exit
" '10 : marks will be remembered for up to 10 previously edited files
" "100 : will save up to 100 lines for each register
" :50 :  up to 50 lines of command-line history will be remembered
" % : saves and restores the buffer list
" n... : where to save the viminfo files
" set viminfo='10,\"100,:50,%,nc:$HOME/.viminfo


" Convenient command to see the difference between the current buffer and the
" file it was loaded from, thus the changes you made.
" Only define it when not defined already.
if !exists(":DiffOrig")
  command DiffOrig vert new | set bt=nofile | r ++edit # | 0d_ | diffthis
		  \ | wincmd p | diffthis
endif

let g:DisableAutoPHPFolding = 1

map <F9> <ESC>:w<Cr>:bro e<Cr>
map <F3> <ESC>:tabp<Cr>
map <F4> <ESC>:tabn<Cr>

filetype plugin on
" au BufNewFile,BufRead *.xml,*.html,*.htm so ~/.vim/plugin/XMLFolding.vim

au! BufRead,BufNewFile *.json set filetype=json 
augroup json_autocmd
  autocmd!
  autocmd FileType json set autoindent
  autocmd FileType json set formatoptions=tcq2l
  autocmd FileType json set textwidth=78 shiftwidth=2
  autocmd FileType json set softtabstop=2 tabstop=8
  autocmd FileType json set expandtab
  autocmd FileType json set foldmethod=syntax
augroup END

"let javaScript_fold=1
set showmatch
map <F12> :q<CR>
set guifont=Monospace\ 8
