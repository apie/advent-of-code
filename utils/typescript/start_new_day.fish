#!/usr/bin/fish
set DAY "$argv"
set PADDAY (printf "%02d" "$DAY")
test $PADDAY -gt 0; or exit 1
# Thx HarmtH for this sed-idea:
# Placeholder is _DAY_ in a template file
set DAYFILE d"$PADDAY".ts
stat -t $DAYFILE; or sed "s/_DAY_/$PADDAY/g" < TEMPLATE.ts > $DAYFILE
set DAYTESTFILE d"$PADDAY"_test.ts
stat -t $DAYTESTFILE; or sed "s/_DAY_/$PADDAY/g" < TEST_TEMPLATE.ts > $DAYTESTFILE

set PREVDAY (expr $PADDAY '-' 1)
set PADPREVDAY (printf "%02d" "$PREVDAY")
grep "import d$PADDAY" run.ts -q; or sed "s/\(import d$PADPREVDAY from \".\/d$PADPREVDAY.ts\";\)/\
\1\n\
import d$PADDAY from \".\/d$PADDAY.ts\";/
s/\(default:\)/\
case \"$DAY\":\n\
        answers = d$PADDAY\(text\);\n\
        break;\n\
    \1/" run.ts -i
../get_problem.bash (basename (pwd)) $DAY
../get_input.bash (basename (pwd)) $DAY
git add $DAYFILE $DAYTESTFILE run.ts d"$PADDAY"a.html
