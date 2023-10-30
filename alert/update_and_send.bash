#!/bin/bash
set -eu
LEADERBOARD_ID=$1
YEAR=$2
CONFIGFILE=$3
./alerter.py $YEAR $LEADERBOARD_ID > $LEADERBOARD_ID/$YEAR/log.txt && ./send_last_log.bash $LEADERBOARD_ID $YEAR $CONFIGFILE

