#!/bin/bash

# get script directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# change to the app directory
cd $DIR/../app

# check if python command is available, if not try running app with python3
if command -v python &> /dev/null; then
    python app.py
else
    python3 app.py
fi

