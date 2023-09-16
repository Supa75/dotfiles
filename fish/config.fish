if status is-interactive
    # Commands to run in interactive sessions can go here
end

# start neofetch
fastfetch

# spicetify add path
fish_add_path /Users/nahalawwad/.spicetify

# neovim config alias
alias nvimrc="nvim ~/.config/nvim/init.lua"
alias lazy="nvim ~/.config/nvim/lua/custom/plugins/plugins.lua"

# alias gcc
alias gcc="gcc-13"
alias g++="g++-13"

# alias python
alias python="python3.11"

# add discocss to $PATH
fish_add_path ~/repo/discocss/

# set TERM variable when using ssh
set -gx TERM xterm-256color

# Created by `pipx` on 2023-09-02 09:35:38
set PATH $PATH /Users/nahalawwad/.local/bin

