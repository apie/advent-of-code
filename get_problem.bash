#!/bin/bash
set -euo pipefail
if [ $# -lt 2 ]
then
  echo 'Provide year and day to download problem for'
  exit 1
fi
DIR=$(dirname "$0")
if [ ! -f "$DIR"/cookie.txt ]
then
  echo 'No cookie found'
  exit 1
fi
COOKIE=$(cat "$DIR"/cookie.txt)
YEAR=$1
DAY=$(($2)) # Convert to int to strip leading zero
TMP_FILENAME="/tmp/aoc-problem.html"
curl "https://adventofcode.com/$YEAR/day/$DAY" -H "Cookie: session=$COOKIE" > $TMP_FILENAME
if [ "$(cat $TMP_FILENAME)" == "Please log in to get problem (need to log in for part 2)." ]
then
    echo 'Expired cookie! Log in again'
    exit 1
fi
# Install pup: `go install github.com/ericchiang/pup@latest`
# Info: https://github.com/ericchiang/pup
# Save part 1 and part 2 as separate files.
P1_FILENAME="$DIR"/$YEAR/d"$(printf "%02da.html" "$DAY")"
cat $TMP_FILENAME | pup 'article:nth-of-type(1)' > $P1_FILENAME
if [ "$(cat $TMP_FILENAME | pup 'article:nth-of-type(2)' | wc -l)" -eq 0 ]
then
    echo 'NOTE: part 2 not unlocked yet!'
else
    P2_FILENAME="$DIR"/$YEAR/d"$(printf "%02db.html" "$DAY")"
    cat $TMP_FILENAME | pup 'article:nth-of-type(2)' > $P2_FILENAME
fi

# If both parts completed, show a message!
grep 'Both parts of this puzzle are complete!' $TMP_FILENAME -q && echo 'Day completely solved!'

