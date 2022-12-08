PROGRAM d8a;
USES sysutils, math;

    FUNCTION answer(filename:string; size:integer) : integer;
    VAR
        grid: array [1..99, 1..99] of integer;
        f: text;
        ch: char;
        i, r, c: integer;
        visible: boolean;
        highest: integer;
    BEGIN
        IF NOT FileExists(filename) THEN BEGIN writeln('file not found: ', filename); halt; END;
        answer := 0;
        assign(f, filename);
        reset(f);
        WHILE not eof(f) DO
            FOR r:=1 TO size DO
                FOR c:=1 TO size+1 DO
                BEGIN
                    read(f, ch);
                    if ch=LineEnding then continue;
                    grid[r][c] := strtoint(trim(ch));
                END;
        close(f);

        FOR r:=1 TO size DO
            FOR c:=1 TO size DO
            BEGIN
                IF (r=1) OR (r=size) OR (c=1) OR (c=size) THEN answer += 1{trees on edge of grid}
                ELSE
                BEGIN
                    {check highest tree left, right, up and down of our position}
                    highest := 0;
                    {L}FOR i:=1 TO c-1 DO highest := max(highest, grid[r][i]);
                    visible := grid[r][c] > highest;
                    IF visible THEN answer += 1;
                    IF visible THEN continue;
                    highest := 0;
                    {R}FOR i:=c+1 TO size DO highest := max(highest, grid[r][i]);
                    visible := grid[r][c] > highest;
                    IF visible THEN answer += 1;
                    IF visible THEN continue;
                    highest := 0;
                    {U}FOR i:=1 TO r-1 DO highest := max(highest, grid[i][c]);
                    visible := grid[r][c] > highest;
                    IF visible THEN answer += 1;
                    IF visible THEN continue;
                    highest := 0;
                    {D}FOR i:=r+1 TO size DO highest := max(highest, grid[i][c]);
                    visible := grid[r][c] > highest;
                    IF visible THEN answer += 1;
                    IF visible THEN continue;
                END;
            END;
    END;
BEGIN{d8a}
    assert(answer('d8.test.1', 5) = 21, 'test 1 faal');
    writeln('answer: ', answer('d8.input', 99));
END.
