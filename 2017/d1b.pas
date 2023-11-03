PROGRAM d1b;
USES sysutils;

    FUNCTION answer(filename:string) : longint;
    VAR
        f: text;
        l: ansistring; {no length limit. 'string' has max length 255}
        i: integer;
        halflen: integer;
        lookpos: integer;
    BEGIN{answer}
        answer := 0;
        assign(f, filename);
        reset(f);
        readln(f, l);
        l := trim(l);
        halflen := length(l) DIV 2;
        writeln(length(l));
        writeln(halflen);
        FOR i:=1 TO length(l) DO
        BEGIN
            writeln(i, ': ',l[i]);
            {calculate lookpos. zero based.}
            lookpos := (i-1 + halflen) mod (halflen * 2);
            writeln('looking at pos: ',lookpos + 1);
            IF l[i] = l[lookpos + 1] THEN answer := answer + strtoint(l[i]);
        END;
        close(f);
        writeln('ans: ',answer);
    END;

CONST
    testfile5 = 'd1.test.5';
    testfile6 = 'd1.test.6';
    testfile7 = 'd1.test.7';
    testfile8 = 'd1.test.8';
    testfile9 = 'd1.test.9';
    filename = 'd1.input';
VAR
    a: longint;
BEGIN{d1b}
    assert(answer(testfile5) = 6, 'test 5 faal');
    assert(answer(testfile6) = 0, 'test 6 faal');
    assert(answer(testfile7) = 4, 'test 7 faal');
    assert(answer(testfile8) = 12, 'test 8 faal');
    assert(answer(testfile9) = 4, 'test 9 faal');
    a := answer(filename);
    assert(a <> 64, 'incorrect');
    writeln('');
    writeln('answer: ', a);
END.
