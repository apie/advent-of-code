#!/bin/bash
set -eu
LEADERBOARD_ID=$1
YEAR=$2
CONFIGFILE=$3
mkdir -p $LEADERBOARD_ID/$YEAR
touch $LEADERBOARD_ID/$YEAR/log.txt
touch $LEADERBOARD_ID/$YEAR/sent.txt
diff $LEADERBOARD_ID/$YEAR/log.txt $LEADERBOARD_ID/$YEAR/sent.txt | grep '<' | ~/.local/bin/telegram-send --config $CONFIGFILE --stdin
cp $LEADERBOARD_ID/$YEAR/log.txt $LEADERBOARD_ID/$YEAR/sent.txt
