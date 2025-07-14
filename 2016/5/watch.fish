#!/usr/bin/fish
while inotifywait -e close_write .
    $argv
end

