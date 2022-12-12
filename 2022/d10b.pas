PROGRAM d10b;
USES sysutils, integerlist;
TYPE
    crt = array[0..5, 0..39] of char;

    FUNCTION answer(filename : string) : crt;
    VAR
        f: text;
        l: string;
        x: integer = 1;
        cycle: integer = 0;
        instructions: TIntegerList;
        row, col: integer;
    BEGIN
        IF NOT FileExists(filename) THEN BEGIN writeln('file not found: ', filename); halt; END;
        instructions := TIntegerList.Create;
        assign(f, filename);
        reset(f);
        WHILE not eof(f) DO
        BEGIN
            readln(f, l);
            instructions.Add(0);
            IF copy(l, 1, 4) = 'addx' THEN
                instructions.Add(strToInt(copy(l, 6, length(l)-5)));
        END;
        close(f);

        FOR row:=0 TO 5 DO
            FOR col:=0 TO 39 DO
                answer[row][col] := '.';

        FOR cycle:=1 TO instructions.Count DO
        BEGIN
            row := (cycle-1) div 40;
            col := (cycle-1) mod 40;
            IF (x-1=col) OR (x=col) OR (x+1=col) THEN
              answer[row][col] := '#';

            inc(x, instructions[cycle-1]);
        END;
        instructions.Free;
        writeln(answer[0]);
        writeln(answer[1]);
        writeln(answer[2]);
        writeln(answer[3]);
        writeln(answer[4]);
        writeln(answer[5]);
    END;
VAR
    a: crt;
BEGIN{d10b}
    writeln('test');
    a := answer('d10.test.2');
    assert(a[0] = '##..##..##..##..##..##..##..##..##..##..');
    assert(a[1] = '###...###...###...###...###...###...###.');
    assert(a[2] = '####....####....####....####....####....');
    assert(a[3] = '#####.....#####.....#####.....#####.....');
    assert(a[4] = '######......######......######......####');
    assert(a[5] = '#######.......#######.......#######.....');
    writeln();
    writeln('answer');
    a := answer('d10.input');
END.
