PROGRAM d2a;
USES sysutils, strutils;

    FUNCTION answer(filename:string) : longint;
    VAR
        f: text;
        l: string;
        x: TStringArray;
        i: integer;
        ri, rowlargest, rowsmallest: integer;
    BEGIN{answer}
        answer := 0;
        assign(f, filename);
        reset(f);
        REPEAT
            readln(f, l);
            l := trim(l);
            writeln(l);
            x := SplitString(l, '	');
            rowlargest := 0;
            rowsmallest := 9999;
            for i:=0 TO length(x)-1 DO
            BEGIN
                ri := strtoint(trim(x[i]));
                writeln(ri);
                IF ri > rowlargest THEN rowlargest := ri;
                IF ri < rowsmallest THEN rowsmallest := ri;
            END;
            writeln(rowlargest, rowsmallest, rowlargest - rowsmallest);
            answer := answer + rowlargest - rowsmallest;
        UNTIL eof(f);
        close(f);
        writeln('ans: ',answer);
    END;

CONST
    testfile1 = 'd2.test.1';
    filename = 'd2.input';
VAR
    a: longint;
BEGIN{d2a}
    assert(answer(testfile1) = 18, 'test 1 faal');
    a := answer(filename);
    writeln('');
    writeln('answer: ', a);
END.
