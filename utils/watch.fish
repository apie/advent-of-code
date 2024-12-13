#!/usr/bin/fish
while inotifywait -e close_write . ../utils/typescript/
    $argv
end

