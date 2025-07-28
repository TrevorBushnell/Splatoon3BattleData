#!/bin/bash

if [[ "$1" == "-b" ]]; then
    python ./data/scripts/battle_json_parser.py
    rm -rf ./data/scripts/__pycache__
elif [[ "$1" == "-s" ]]; then
    python ./data/scripts/salmon_run_json_parser.py
    rm -rf ./data/scripts/__pycache__
else
    echo "Usage: $0 [-b|-s]"
    echo "  -b    Run script_b.py"
    echo "  -s    Run script_s.py"
    exit 1
fi