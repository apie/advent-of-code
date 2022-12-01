#!/bin/bash
set -eu
YEAR=$1
touch $YEAR/log.txt
touch $YEAR/sent.txt
diff $YEAR/log.txt $YEAR/sent.txt | grep '<' | ~/.local/bin/telegram-send --config ~/telegram/send/denicksbot/oud-scintilla-aoc.conf --stdin
cp $YEAR/log.txt $YEAR/sent.txt
