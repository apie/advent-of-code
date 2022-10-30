#!/bin/bash
set -euo pipefail
YEAR=$1
UPDATE_FREQ_MINUTES=$2
mkdir -p $YEAR
cp send_last_log.bash $YEAR/
cd $YEAR
tmux new-session -d -s "aoc${YEAR}" "../alerter.py ${YEAR} ${UPDATE_FREQ_MINUTES} >> log.txt";
touch log.txt
#split vertical
tmux split-window -v "/bin/bash -c 'while inotifywait -e modify log.txt; do ./send_last_log.bash; done;'";
tmux attach-session -t "aoc${YEAR}"

