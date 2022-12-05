PROGRAM d5a;
USES sysutils;

FUNCTION answer(filename:string) : string;
VAR
    f: text;
    l: string;
    i, amt, src, dest: integer;
    stack: array[1..9] of string;
BEGIN
    answer := '';
    FOR i := 1 TO 9 DO stack[i] := '';
    assign(f, filename);
    reset(f);
    WHILE not eof(f) DO
    BEGIN
        {read stacks}
        readln(f, l);
        IF pos(' 1 ', l) > 0 THEN break;
        FOR i := 1 TO 9 DO stack[i] += trim(copy(l, -2+4*i, 1));
    END;
    readln(f, l);
    WHILE not eof(f) DO
    BEGIN
        {read instruction}
        readln(f, l);
        amt := strtoint(trim(copy(l, pos('move', l)+5, 2)));
        src := strtoint(trim(copy(l, pos('from', l)+5, 2)));
        dest := strtoint(trim(copy(l, pos('to', l)+3, 1)));
        IF (length(stack[src]) > 0) THEN
        BEGIN
            stack[dest] := copy(stack[src], 1, amt) + stack[dest];
            stack[src] := copy(stack[src], 1+amt, length(stack[src]));
        END;
    END;
    close(f);
    FOR i := 1 TO 9 DO
    BEGIN
        IF (length(stack[i]) > 0) THEN answer += trim(stack[i][1]);
    END;
    answer := trim(answer);
END;

CONST
    testfile = 'd5.test.1';
    filename = 'd5.input';
VAR
    a: string;
BEGIN{d5a}
    assert(answer(testfile) = 'MCD', 'test faal');
    a := answer(filename);
    writeln('');
    writeln('answer: ', answer(filename));
END.
