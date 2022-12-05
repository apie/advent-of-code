PROGRAM d3b;

    FUNCTION score(c:char) : integer;
    CONST
        lowA = ord('a');
        capA = ord('A');
    BEGIN
        {lowercase}
        IF ord(c) >= lowA THEN score := ord(c) - lowA + 1
        {uppercase}
        ELSE score := ord(c) - capA + 27;
    END;

    FUNCTION answer(filename:string) : integer;
    VAR
        f: text;
        compartments: array[1..3] of string;
        c: char;
        i: integer;
        totscore: integer = 0;
    BEGIN
        assign(f, filename);
        reset(f);
        WHILE not eof(f) DO
        BEGIN
            FOR i := 1 TO 3 DO readln(f, compartments[i]);
            FOR i := 1 TO 50 DO
            BEGIN
                c := compartments[1][i];
                IF (pos(c, compartments[2]) > 0) AND (pos(c, compartments[3]) > 0) THEN
                BEGIN
                    totscore += score(c);
                    break;
                END;
            END;
        END;
        close(f);
        answer := totscore;
    END;

CONST
    testfile = 'd3.test.1';
    filename = 'd3.input';
VAR
    a : integer;
BEGIN{d3b}
    assert(18=score('r'));
    assert(52=score('Z'));
    assert(answer(testfile) = 70, 'test faal');
    a := answer(filename);
    writeln('');
    writeln('answer: ', a);
END.
