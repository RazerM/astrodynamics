#!/bin/bash

set -e
set -x

if [[ "$(uname -s)" == 'Darwin' ]]; then
    brew install findutils
    gfind $HOME/Library/Caches/pip -type f -name '*.whl'  
else
    find $HOME/.cache/pip -type f -name '*.whl'  
fi
