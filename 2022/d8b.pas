PROGRAM d8b;
USES sysutils, math;

    FUNCTION answer(filename:string; size:integer) : int64;
    VAR
        grid: array [1..99, 1..99] of integer;
        f: text;
        ch: char;
        i, r, c: integer;
        vdist: array[1..4] of integer;
        ans, scenic_score: int64;
    BEGIN
        IF NOT FileExists(filename) THEN BEGIN writeln('file not found: ', filename); halt; END;
        answer := 0;
        ans := 0;
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
                IF (r=1) OR (r=size) OR (c=1) OR (c=size) THEN {trees on edge of grid}
                ELSE
                BEGIN
                    {check vdist left, right, up and down of our position}
                    {L}FOR i:=c-1 DOWNTO 1 DO
                        IF (i=1) OR (grid[r][i] >= grid[r][c]) THEN
                        BEGIN
                            vdist[1] := abs(c-i);
                            break;
                        END;
                    {R}FOR i:=c+1 TO size DO
                        IF (i=size) OR (grid[r][i] >= grid[r][c]) THEN
                        BEGIN
                            vdist[2] := abs(c-i);
                            break;
                        END;
                    {U}FOR i:=r-1 DOWNTO 1 DO
                        IF (i=1) OR (grid[i][c] >= grid[r][c]) THEN
                        BEGIN
                            vdist[3] := abs(r-i);
                            break;
                        END;
                    {D}FOR i:=r+1 TO size DO
                        IF (i=size) OR (grid[i][c] >= grid[r][c]) THEN
                        BEGIN
                            vdist[4] := abs(r-i);
                            break;
                        END;
                    scenic_score := vdist[1] * vdist[2] * vdist[3] * vdist[4];
                    {needed since we may not assign this big numbers to answer?}
                    ans := max(ans, scenic_score);
                END;
            END;
        answer := ans;
    END;
VAR
    a: int64;
BEGIN{d8b}
    assert(answer('d8.test.1', 5) = 8, 'test 1 faal');
    a := answer('d8.input', 99);
    assert(a > 32736); 
    assert(a < 5517072); 
    writeln('answer: ', a);
END.
