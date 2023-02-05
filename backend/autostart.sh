#!/bin/bash


if [[ ! -f ~/.pyenv/versions/3.9.6/bin/python3.9 ]]
then
  pyenv install 3.9.6
fi 

pyenv local 3.9.6
poetry install
poetry env use ~/.pyenv/versions/3.9.6/bin/python3.9
poetry shell
