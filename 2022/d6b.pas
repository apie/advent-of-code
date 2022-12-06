PROGRAM d6b;
USES sysutils;

FUNCTION answer(filename:string) : integer;
CONST
    MSG_LEN = 14;
VAR
    f: text;
    c: char;
    l: string = '';
    i: integer = 0;
    j, p: integer;
    doubles_found: boolean;
BEGIN
    answer := 0;
    assign(f, filename);
    reset(f);
    REPEAT
        i += 1;
        read(f, c);
        l += c;
        IF length(l) < MSG_LEN THEN continue;
        IF length(l) > MSG_LEN THEN l := copy(l, 2, MSG_LEN+1);
        doubles_found := false;
        FOR j:=1 TO MSG_LEN DO
        BEGIN
            p := pos(l[j], l);
            IF (p <> j) AND (p > 0) THEN doubles_found := true;
        END;
        IF doubles_found = false THEN answer := i;
        IF answer > 0 THEN break;
    UNTIL eof(f);
    close(f);
END;

CONST
    testfile1 = 'd6.test.1';
    testfile2 = 'd6.test.2';
    testfile3 = 'd6.test.3';
    testfile4 = 'd6.test.4';
    testfile5 = 'd6.test.5';
    filename = 'd6.input';
VAR
    a: integer;
BEGIN{d6b}
    assert(answer(testfile1) = 19, 'test 1 faal');
    assert(answer(testfile2) = 23, 'test 2 faal');
    assert(answer(testfile3) = 23, 'test 3 faal');
    assert(answer(testfile4) = 29, 'test 4 faal');
    assert(answer(testfile5) = 26, 'test 5 faal');
    writeln('');
    a := answer(filename);
    writeln('answer: ', a);
END.
