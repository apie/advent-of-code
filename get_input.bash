#!/bin/bash
DIR=$(dirname "$0")
if [ ! -f "$DIR"/cookie.txt ]
then
  echo 'No cookie found'
  exit 1
fi
COOKIE=$(cat "$DIR"/cookie.txt)
YEAR=2019
DAY=$(($1)) # Convert to int to strip leading zero
if [ $# -gt 0 ]
then
  curl "https://adventofcode.com/$YEAR/day/$DAY/input" -H "Cookie: session=$COOKIE" > "$DIR"/$YEAR/"$(printf "%.2d.input" "$DAY")"
fi
