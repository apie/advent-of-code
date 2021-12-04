#!/bin/bash
echo 'd2a'
rm -f d2_test.db
cat -n d2.test|awk '{ print $1","$2","$3 }'|sed -e '1iid,op,value'|sqlite-utils insert d2_test.db test - --csv
echo 'test'
sqlite3 d2_test.db < d2a.sql

rm -f d2.db
cat -n d2.input|awk '{ print $1","$2","$3 }'|sed -e '1iid,op,value'|sqlite-utils insert d2.db test - --csv
echo 'answer'
sqlite3 d2.db < d2a.sql

