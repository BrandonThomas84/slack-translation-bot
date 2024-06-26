#!/bin/bash

# get script directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# change to the app directory
cd $DIR/../app

pip install Flask slack_sdk google-cloud-translate python-dotenv
