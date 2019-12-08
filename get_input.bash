#!/bin/bash
if [ ! -f cookie.txt ]
then
  echo 'No cookie found'
  exit 1
fi
COOKIE=`cat cookie.txt`
YEAR=2019
DAY=$1
if [ $# -gt 0 ]
then
  curl "https://adventofcode.com/$YEAR/day/$DAY/input" -H "Cookie: session=$COOKIE" > $YEAR/"$(printf "%.2d.in" "$DAY")"
fi
