PROGRAM d3a;
USES sysutils, strutils;


    FUNCTION answer(filename:string) : longint;
    VAR
        file_text: text;
        line_s: string;
        sq: longint;
        {determined by taking sqrt(input) / 2}
        memory: array [-269..269,-269..269] of longint;
        i, x,y: longint;
        dir: char;

        PROCEDURE initmem;
        VAR
          i, j: Integer;
        BEGIN{initmem}
            FOR i := low(memory) TO high(memory) DO
                FOR j := low(memory[i]) TO high(memory[i]) DO
                    memory[i][j] := 0;
        END;
    BEGIN{answer}
        initmem;
        answer := 0;
        assign(file_text, filename);
        reset(file_text);
        readln(file_text, line_s);
        sq := strtoint(line_s);
        writeln(sq);
        writeln(round(sqrt(sq))+1);
        close(file_text);
        x := 0;
        y := 0;
        dir := 'r';
        FOR i := 1 TO sq DO
        BEGIN
            {writeln(x, ' ', y, ' ', dir, ' ', i);}
            IF i = sq THEN answer := abs(x)+abs(y);
            memory[x][y] := i;
            IF dir='r' THEN
            BEGIN
              inc(x);
              IF memory[x][y-1] = 0 THEN dir := 'u';
            END
            ELSE IF dir='l' THEN
            BEGIN
                inc(x, -1);
                IF memory[x][y+1] = 0 THEN dir := 'd';
            END
            ELSE IF dir='u' THEN
            BEGIN
                inc(y, -1);
                IF memory[x-1][y] = 0 THEN dir := 'l';
            END
            ELSE IF dir='d' THEN
            BEGIN
                inc(y, 1);
                IF memory[x+1][y] = 0 THEN dir := 'r';
            END
        END;
        writeln('ans: ',answer);
    END;

CONST
    testfile1 = 'd3.test.1';
    testfile2 = 'd3.test.2';
    testfile3 = 'd3.test.3';
    testfile4 = 'd3.test.4';
    filename = 'd3.input';
VAR
    a: longint;
BEGIN{d3a}
    assert(answer(testfile1) = 0, 'test 1 faal');
    assert(answer(testfile2) = 3, 'test 2 faal');
    assert(answer(testfile3) = 2, 'test 3 faal');
    assert(answer(testfile4) = 31, 'test 4 faal');
    a := answer(filename);
    writeln('');
    writeln('answer: ', a);
END.
