#!/bin/bash

set -e

BUILD_DIR=/sdist/

for dir in ./netbox*; do
    if [ -d "$dir" ] && [ -f "${dir}/setup.py" ]; then
    	cd $dir && pip install -e . --user && cd ../
    fi
done
