# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
# exists.
# see /usr/share/doc/bash/examples/startup-files for examples.
# the files are located in the bash-doc package.

# the default umask is set in /etc/profile; for setting the umask
# for ssh logins, install and configure the libpam-umask package.
#umask 022

# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
	. "$HOME/.bashrc"
    fi
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi
export EDITOR=vim

function xgrep() {
        find -H `pwd` -name "*.$1" | xargs grep "$2" --exclude-dir=.svn -n
}
function pygrep() {
        xgrep 'py' $* | grep -v "/migrations/"
}

function duplicates() {
    sort | uniq -d
}

function filextensions() {
    find . -type f | sed 's/.*\/\([^/]\+\)$/\1/g' | grep '\.' | sed 's/^.*\.\(\S\+\)$/\1/g' | sort -u
}

source ~/.django-project
source ~/.current-django-project
source ~/.svnhelpers
source ~/.elixir
