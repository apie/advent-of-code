PROGRAM d4b;
USES sysutils, strutils;

    FUNCTION anagram(const s1, s2:string) : boolean;
    VAR
        t1, t2: string;
        i,j: integer;
    BEGIN
        anagram := false;
        t1 := s1;
        t2 := s2;
        IF length(t1) <> length(t2) THEN anagram := false
        ELSE
        BEGIN
          FOR i:=1 TO length(t1) DO
          BEGIN
              FOR j:=1 TO length(t1) DO
            IF t1[i] = t2[j] THEN
            BEGIN
                t1[i] := '.';
                t2[j] := '.';
            END;
          END;
          IF t1 = t2 THEN anagram := true;
        END;
    END;

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
                        IF anagram(x[i], x[j]) THEN valid := false;
            IF valid THEN inc(answer);
        UNTIL eof(f);
        close(f);
        writeln('ans: ',answer);
    END;

CONST
    testfile4 = 'd4.test.4';
    testfile5 = 'd4.test.5';
    testfile6 = 'd4.test.6';
    testfile7 = 'd4.test.7';
    testfile8 = 'd4.test.8';
    filename = 'd4.input';
VAR
    a: longint;
BEGIN{d4b}
    assert(answer(testfile4) = 1, 'test 4 faal');
    assert(answer(testfile5) = 0, 'test 5 faal');
    assert(answer(testfile6) = 1, 'test 6 faal');
    assert(answer(testfile7) = 1, 'test 7 faal');
    assert(answer(testfile8) = 0, 'test 8 faal');
    a := answer(filename);
    writeln('');
    writeln('answer: ', a);
END.
