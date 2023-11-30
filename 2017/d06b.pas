PROGRAM d6b;
USES sysutils, strutils;

    FUNCTION answer(filename:string) : longint;
    VAR
        file_text: text;
        line_s: string;
        words: TStringArray;
        cycle: integer = 0;
        findwordstatecycle: integer = 0;
        i,j: integer;
        i_highestbank, highestbank: integer;
        banks: array [1..16] of integer;
        i_states: integer = 1;
        states: array [1..8000] of string;
        wordstate: string;
        findwordstate: string;

        PROCEDURE printbanks;
        VAR i: integer;
        BEGIN
{           write('cycle ',cycle,'. banks: ');
            FOR i:=1 TO length(words) DO
                write(banks[i]);
            writeln();
}       END;

        PROCEDURE findbankwithmostblocks;
        VAR i: integer;
        BEGIN
            highestbank := -1;
            i_highestbank := -1;
            FOR i:=1 TO length(words) DO
                IF banks[i] > highestbank THEN
                BEGIN
                    highestbank := banks[i];
                    i_highestbank := i;
                END;
{           writeln('bank ',i_highestbank,' has the most blocks: ',highestbank);
}       END;

        PROCEDURE redistribute;
        BEGIN
            WHILE highestbank > 0 DO
            BEGIN
                i_highestbank := i_highestbank MOD (length(words)+1);
                IF i_highestbank = 0 THEN inc(i_highestbank);
{               writeln('>> at bank ',i_highestbank, ', value: ',banks[i_highestbank]);
}               inc(banks[i_highestbank]);
                inc(highestbank, -1);
                inc(i_highestbank);
            END;
        END;
    BEGIN{answer}
        answer := 0;
        assign(file_text, filename);
        reset(file_text);
        {init}
        FOR i:=1 TO length(banks) DO
            banks[i] := 0;
        FOR i:=1 TO length(states) DO
            states[i] := 'x';

        {read input into banks}
        REPEAT
            readln(file_text, line_s);
            line_s := trim(line_s);
            words := SplitString(line_s, '	');
            writeln('length words: ',length(words));
            FOR i:=1 TO length(words) DO
                banks[i] := strtoint(trim(words[i-1]));
        UNTIL eof(file_text);
        close(file_text);

        findwordstate := '';
        REPEAT
            printbanks;
            inc(cycle);
            findbankwithmostblocks;
            {take blocks from highest}
            banks[i_highestbank] := 0;
            {move to next bank}
            inc(i_highestbank);
            {redistribute blocks over banks. moving right one step every time, wrapping around to the beginning.}
            redistribute;

            {if state seen before. save}
            {if state seen again. stop}
            wordstate := '';
            FOR j:=1 TO length(words) DO
                wordstate := wordstate + IntToStr(banks[j]);
            IF wordstate = findwordstate THEN answer := cycle - findwordstatecycle;
            FOR i:=1 TO i_states DO
                IF (findwordstate = '') AND (states[i] = wordstate) THEN
                BEGIN
                    writeln('found at cycle ', cycle);
                    findwordstate := wordstate;
                    findwordstatecycle := cycle;
                END;

            IF (findwordstate = '') THEN
            BEGIN
                {save state}
                inc(i_states);
                states[i_states] := wordstate;
            END;
        UNTIL answer > 0;
        writeln('ans: ',answer);
    END;

CONST
    testfile1 = 'd6.test.1';
    filename = 'd6.input';
VAR
    a: longint;
BEGIN{d6b}
    assert(answer(testfile1) = 4, 'test 1 faal');
    a := answer(filename);
    writeln('');
    writeln('answer: ', a);
END.
