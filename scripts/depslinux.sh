#!/bin/bash

sudo apt install curl git-core gcc make zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev libssl-dev
git clone https://github.com/pyenv/pyenv.git $HOME/.pyenv


echo export PYENV_ROOT="$HOME/.pyenv" >> ~/.bashrc
echo export PATH="$PYENV_ROOT/bin:$PATH" >> ~/.bashrc
echo "\n"
echo "if command -v pyenv 1>/dev/null 2>&1; then
  > echo  eval "$(pyenv init -)"
fi"

curl -sSL https://install.python-poetry.org | python3 -

export PATH="/home/$USER/.local/bin:$PATH"
source ~/.bashrc
