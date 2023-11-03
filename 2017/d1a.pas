PROGRAM d1a;
USES sysutils;

    FUNCTION answer(filename:string) : longint;
    VAR
        f: text;
        c: char;
        dig: longint = -1;
    BEGIN{answer}
        answer := 0;
        assign(f, filename);
        reset(f);
        REPEAT
            read(f, c);
            IF trim(c) = '' THEN continue;
            IF strtoint(c) = dig THEN answer := answer + dig;
            dig := strtoint(c);
            writeln(dig);
        UNTIL eof(f);
        reset(f);
        read(f, c);
        IF strtoint(c) = dig THEN answer := answer + dig;
        close(f);
        writeln('ans: ',answer);
    END;

CONST
    testfile1 = 'd1.test.1';
    testfile2 = 'd1.test.2';
    testfile3 = 'd1.test.3';
    testfile4 = 'd1.test.4';
    filename = 'd1.input';
VAR
    a: longint;
BEGIN{d1a}
    assert(answer(testfile1) = 3, 'test 1 faal');
    assert(answer(testfile2) = 4, 'test 2 faal');
    assert(answer(testfile3) = 0, 'test 3 faal');
    assert(answer(testfile4) = 9, 'test 4 faal');
    a := answer(filename);
    writeln('');
    writeln('answer: ', a);
END.
