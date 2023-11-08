PROGRAM d2b;
USES sysutils, strutils;

    FUNCTION answer(filename:string) : longint;
    VAR
        f: text;
        l: string;
        x: TStringArray;
        i, j: integer;
        ri: integer;
        row: array of integer;
    BEGIN{answer}
        answer := 0;
        assign(f, filename);
        reset(f);
        REPEAT
            row := nil;
            setlength(row, 100);
            readln(f, l);
            l := trim(l);
            writeln(l);
            x := SplitString(l, '	');
            FOR i:=0 TO length(x)-1 DO
                row[i] := strtoint(trim(x[i]));
            FOR i:=0 TO length(x)-1 DO
                FOR j:=0 TO length(x)-1 DO
                    IF i<>j THEN
                        IF (row[i] MOD row[j] = 0) THEN
                        BEGIN
                            writeln('-> ',row[i], row[j]);
                            answer := answer + (row[i] DIV row[j]);
                        END;
        UNTIL eof(f);
        close(f);
        writeln('ans: ',answer);
    END;

CONST
    testfile = 'd2.test.2';
    filename = 'd2.input';
VAR
    a: longint;
BEGIN{d2b}
    assert(answer(testfile) = 9, 'test 1 faal');
    a := answer(filename);
    writeln('');
    writeln('answer: ', a);
END.
