PROGRAM d3b;
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
                    memory[i,j] := 0;
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
            IF i = 1 THEN memory[x,y] := 1
            ELSE
            BEGIN
                {sum surrounding cells:
                    - - -
                    - o -
                    - - -       }
                memory[x  ,y  ] :=
                memory[x+1,y  ] +
                memory[x+1,y+1] +
                memory[x+1,y-1] +
                memory[x-1,y  ] +
                memory[x-1,y+1] +
                memory[x-1,y-1] +
                memory[x  ,y+1] +
                memory[x  ,y-1];
            END;
            {writeln(x, ' ', y, ' ', dir, ' ', memory[x,y]);}
            IF memory[x,y] > sq THEN
            BEGIN
                answer := memory[x,y];
                break;
            END;

            IF dir='r' THEN
            BEGIN
                inc(x);
                IF memory[x,y-1] = 0 THEN dir := 'u';
            END
            ELSE IF dir='l' THEN
            BEGIN
                inc(x, -1);
                IF memory[x,y+1] = 0 THEN dir := 'd';
            END
            ELSE IF dir='u' THEN
            BEGIN
                inc(y, -1);
                IF memory[x-1,y] = 0 THEN dir := 'l';
            END
            ELSE IF dir='d' THEN
            BEGIN
                inc(y, 1);
                IF memory[x+1,y] = 0 THEN dir := 'r';
            END
        END;
        writeln('ans: ',answer);
    END;

CONST
    testfile5 = 'd3.test.5';
    testfile6 = 'd3.test.6';
    filename = 'd3.input';
VAR
    a: longint;
BEGIN{d3b}
    assert(answer(testfile5) = 122, 'test 5 faal');
    assert(answer(testfile6) = 25, 'test 6 faal');
    a := answer(filename);
    writeln();
    writeln('answer: ', a);
END.
