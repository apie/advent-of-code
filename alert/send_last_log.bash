#!/bin/bash
set -euo pipefail
diff log.txt sent.txt | grep '<' | ~/.local/bin/telegram-send --config ~/telegram/send/denicksbot/oud-scintilla-aoc.conf --stdin
cp log.txt sent.txt
