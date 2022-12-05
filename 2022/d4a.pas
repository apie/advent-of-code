PROGRAM d4a;
USES sysutils;

FUNCTION answer(filename:string) : integer;
VAR
    f: text;
    l: string;
    pair: array[1..2] of string;
    range: array[1..4] of integer;
BEGIN
    answer := 0;
    assign(f, filename);
    reset(f);
    WHILE not eof(f) DO
    BEGIN
        readln(f, l);
        pair[1] := copy(l, 1          , pos(',', l)-1);
        pair[2] := copy(l, pos(',', l)+1, length(l));
        range[1] := strtoint(copy(pair[1], 1, pos('-', pair[1])-1));
        range[2] := strtoint(copy(pair[1], pos('-', pair[1])+1, length(pair[1])));
        range[3] := strtoint(copy(pair[2], 1, pos('-', pair[2])-1));
        range[4] := strtoint(copy(pair[2], pos('-', pair[2])+1, length(pair[2])));
        {If one range fully contains the other, add it to our count}
        {left pair contains right pair}
        IF (range[1] <= range[3]) AND (range[2] >= range[4]) THEN answer += 1
        {right pair contains left pair}
        ELSE IF (range[3] <= range[1]) AND (range[4] >= range[2]) THEN answer += 1;
    END;
    close(f);
END;

CONST
    testfile = 'd4.test.1';
    filename = 'd4.input';
VAR
    a : integer;
BEGIN{d4a}
    assert(answer(testfile) = 2, 'test faal');
    a := answer(filename);
    writeln('');
    writeln('answer: ', a);
END.
