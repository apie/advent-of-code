#!/bin/bash
set -eu
LEADERBOARD_ID=$1
YEAR=$2
CONFIGFILE=$3
mkdir -p $LEADERBOARD_ID/$YEAR
touch $LEADERBOARD_ID/$YEAR/log.txt
./alerter.py $YEAR $LEADERBOARD_ID > $LEADERBOARD_ID/$YEAR/log.txt && ./send_last_log.bash $LEADERBOARD_ID $YEAR $CONFIGFILE

