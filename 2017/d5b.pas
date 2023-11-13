PROGRAM d5b;
USES sysutils;


    FUNCTION answer(filename:string) : longint;
    CONST
        STOP = 6666;
    VAR
        file_text: text;
        line_s: string;
        instruction: integer;
        instructions: array of integer;
        i_l, cur, newpos, offset: integer;
    BEGIN{answer}
        answer := 0;
        instructions := nil;
        setlength(instructions, 1100);
        FOR i_l := 1 TO length(instructions)-1 DO instructions[i_l] := STOP;
        assign(file_text, filename);
        reset(file_text);
        i_l := 1;
        REPEAT
            readln(file_text, line_s);
            instruction := strtoint(line_s);
            instructions[i_l] := instruction;
            inc(i_l);
        UNTIL eof(file_text);
        close(file_text);
        cur := 1;
        REPEAT
            offset := instructions[cur];
            newpos := cur + offset;
            {jump}
            {increment old instruction}
            IF offset >= 3 THEN inc(instructions[cur], -1)
            ELSE inc(instructions[cur]);
            {increment n of steps}
            inc(answer);
            cur := newpos;
        UNTIL instructions[cur] = STOP;
        writeln('ans: ',answer);
    END;

CONST
    testfile1 = 'd5.test.1';
    filename = 'd5.input';
VAR
    a: longint;
BEGIN{d5b}
    assert(answer(testfile1) = 10, 'test 1 faal');
    a := answer(filename);
    writeln();
    writeln('answer: ', a);
END.
