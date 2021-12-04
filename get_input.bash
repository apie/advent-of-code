#!/bin/bash
if [ $# -eq 0 ]
then
  echo 'Provide day to download input for'
  exit 1
fi
DIR=$(dirname "$0")
if [ ! -f "$DIR"/cookie.txt ]
then
  echo 'No cookie found'
  exit 1
fi
COOKIE=$(cat "$DIR"/cookie.txt)
YEAR=2021
DAY=$(($1)) # Convert to int to strip leading zero
curl "https://adventofcode.com/$YEAR/day/$DAY/input" -H "Cookie: session=$COOKIE" > "$DIR"/$YEAR/d"$(printf "%.d.input" "$DAY")"
