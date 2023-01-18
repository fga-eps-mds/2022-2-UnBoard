#!/bin/bash

sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl

curl -sSL https://install.python-poetry.org | python3 -

export PATH="/home/$USER/.local/bin:$PATH"
source ~/.bashrc
