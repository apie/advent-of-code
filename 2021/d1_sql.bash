#!/bin/bash
cat -n d1.input|awk '{ print $1","$2 }'|sed -e '1iid,value'|sqlite-utils memory - "$(cat d1a.sql)" --table
cat -n d1.input|awk '{ print $1","$2 }'|sed -e '1iid,value'|sqlite-utils memory - "$(cat d1b.sql)" --table
