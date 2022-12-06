PROGRAM d3;
USES sysutils;

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
    l: string = '';
    len,
    half: integer;
    compartments: array[1..2] of string;
    c: char;
    i: integer;
    totscore: integer = 0;
BEGIN
    IF NOT FileExists(filename) THEN writeln('file not found: ', filename);
    assign(f, filename);
    reset(f);
    WHILE not eof(f) DO
    BEGIN
        readln(f, l);
        len := length(l);
        half := round(len/2);
        compartments[1] := copy(l,      1, half);
        compartments[2] := copy(l, half+1, len);
        FOR i := 1 TO 50 DO
        BEGIN
            c := compartments[1][i];
            IF pos(c, compartments[2]) > 0 THEN
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
BEGIN
    assert(1=score('a'));
    assert(27=score('A'));
    assert(answer(testfile) = 157, 'test faal');
    a := answer(filename);
    assert(a > 7862);
    writeln('answer: ', a);
END.
