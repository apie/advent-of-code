PROGRAM d4a;
USES sysutils, strutils;

    FUNCTION answer(filename:string) : longint;
    VAR
        f: text;
        l: string;
        x: TStringArray;
        i, j: integer;
        valid: boolean;
    BEGIN{answer}
        answer := 0;
        assign(f, filename);
        reset(f);
        REPEAT
            readln(f, l);
            l := trim(l);
            writeln(l);
            x := SplitString(l, ' ');
            valid := true;
            FOR i:=0 TO length(x)-1 DO
                FOR j:=0 TO length(x)-1 DO
                    IF i<>j THEN
                        IF (x[i] = x[j]) THEN
                        BEGIN
                            writeln('-> ', x[i], x[j]);
                            valid := false;
                        END;
            IF valid THEN answer := answer + 1;
        UNTIL eof(f);
        close(f);
        writeln('ans: ',answer);
    END;

CONST
    testfile1 = 'd4.test.1';
    testfile2 = 'd4.test.2';
    testfile3 = 'd4.test.3';
    filename = 'd4.input';
VAR
    a: longint;
BEGIN{d4a}
    assert(answer(testfile1) = 1, 'test 1 faal');
    assert(answer(testfile2) = 0, 'test 2 faal');
    assert(answer(testfile3) = 1, 'test 3 faal');
    a := answer(filename);
    writeln('');
    writeln('answer: ', a);
END.
