#!/bin/bash
# Check if script still exits OK. If not, cookie might be expired. Send a message about it.
set -eu
SCRIPT_DIR="$(readlink -f "${BASH_SOURCE}")"
cd $(dirname $SCRIPT_DIR)
LEADERBOARD_ID=$1
YEAR=$2
CONFIGFILE=$3
./alerter.py $YEAR $LEADERBOARD_ID || ~/.local/bin/telegram-send --config $CONFIGFILE 'got error. aoc cookie expired?'
