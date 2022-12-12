PROGRAM d10a;
USES sysutils, math, integerlist;

    FUNCTION answer(filename : string) : int64;
    VAR
        f: text;
        l: string;
        x: integer = 1;
        cycle: integer = 0;
        instructions: TIntegerList;
    BEGIN
        IF NOT FileExists(filename) THEN BEGIN writeln('file not found: ', filename); halt; END;
        instructions := TIntegerList.Create;
        answer := 0;
        assign(f, filename);
        reset(f);
        cycle := 0;
        WHILE not eof(f) DO
        BEGIN
            readln(f, l);
    {       writeln(l);}
            CASE copy(l, 1, 4) OF
                'noop': instructions.Add(0);
                'addx':
                BEGIN
                    instructions.Add(0);
                    instructions.Add(strToInt(copy(l, 6, length(l)-5)));
                END;
            END;
        END;
        close(f);

        FOR cycle:=1 TO instructions.Count DO
        BEGIN
            IF (cycle=20) OR (cycle=60) OR (cycle=100) OR (cycle=140) OR (cycle=180) OR (cycle=220) THEN
            BEGIN
                writeln('cycle: ', cycle, '. x=', x);
                answer += (cycle * x);
            END;
            writeln('cycle: ', cycle, '. x=', x);
            inc(x, instructions[cycle-1]);
        END;
        instructions.Free;
    END;
VAR
    a: int64;
BEGIN{d10a}
    assert(answer('d10.test.1') = 0, 'test 1 faal');
    assert(answer('d10.test.2') = 13140, 'test 2 faal');
    a := answer('d10.input');
    assert(a < 17520);
    writeln('answer: ', a);
END.
