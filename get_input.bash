#!/bin/bash
set -euo pipefail
if [ $# -lt 2 ]
then
  echo 'Provide year and day to download input for'
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
FILENAME="$DIR"/$YEAR/d"$(printf "%.d.input" "$DAY")"
curl "https://adventofcode.com/$YEAR/day/$DAY/input" -H "Cookie: session=$COOKIE" > $FILENAME
if [ "$(cat $FILENAME)" == "Puzzle inputs differ by user.  Please log in to get your puzzle input." ]
then
    echo 'Expired cookie! Log in again'
    exit 1
fi
