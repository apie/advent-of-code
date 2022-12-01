#!/bin/bash
set -euo pipefail
YEAR=$1
mkdir -p $YEAR
cp send_last_log.bash $YEAR/
cd $YEAR
touch log.txt
tmux new-session -d -s "aoc${YEAR}" "/bin/bash -c 'while inotifywait -e modify log.txt; do ./send_last_log.bash; done;'";
#tmux attach-session -t "aoc${YEAR}"

