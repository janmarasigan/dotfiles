#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

# Created by `pipx` on 2024-05-22 06:04:15
export PATH="$PATH:/home/jan/.local/bin"

eval "$(register-python-argcomplete pipx)"

export EDITOR=/usr/bin/nano
#export GTK_USE_PORTAL=1 firefox
source /usr/share/nvm/init-nvm.sh

export SSH_AUTH_SOCK=$XDG_RUNTIME_DIR/ssh-agent.socket

# mount backup ssd similar to how thunar does it automatically
#gio mount --device=/dev/sda2 /run/media/jan/Backup

alias livetl='~/Programs/stream-translator/venv/bin/python ~/Programs/stream-translator/translator.py --model medium --language Japanese --task translate'
