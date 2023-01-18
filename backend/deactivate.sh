#!/bin/bash

black .
flake8 . --select BLK --exclude=env --show-source1
deactivate
