#!/bin/bash

yes | brew install openssl readline sqlite3 xz zlib

curl -sSL https://install.python-poetry.org | python3 -

export PATH="/home/$USER/.local/bin:$PATH"
source ~/.bashrc
