PROGRAM d5a;
USES sysutils;


    FUNCTION answer(filename:string) : longint;
    CONST
        STOP = 6666;
    VAR
        file_text: text;
        line_s: string;
        instructions: array of integer;
        i_l, cur, newpos: integer;
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
            instructions[i_l] := strtoint(line_s);
            inc(i_l);
        UNTIL eof(file_text);
        close(file_text);
        cur := 1;
        REPEAT
            newpos := cur + instructions[cur];
            {increment old instruction}
            inc(instructions[cur]);
            {increment n of steps}
            inc(answer);
            {jump}
            cur := newpos;
        UNTIL instructions[cur] = STOP;
        writeln('ans: ',answer);
    END;

CONST
    testfile1 = 'd5.test.1';
    filename = 'd5.input';
VAR
    a: longint;
BEGIN{d5a}
    assert(answer(testfile1) = 5, 'test 1 faal');
    a := answer(filename);
    writeln();
    writeln('answer: ', a);
END.
