PROGRAM d4a;
USES sysutils, strutils;

    FUNCTION answer(filename:string) : longint;
    VAR
        file_text: text;
        line_s: string;
        words: TStringArray;
        i_currentword, i_foundword: integer;
        valid: boolean;
    BEGIN{answer}
        answer := 0;
        assign(file_text, filename);
        reset(file_text);
        REPEAT
            {check each line}
            readln(file_text, line_s);
            line_s := trim(line_s);
            words := SplitString(line_s, ' ');
            valid := true;
            {go through each word on the line and compare with the other words on the line. if a word appears more than once, mark line as invalid}
            FOR i_currentword:=0 TO length(words)-1 DO
            BEGIN
                i_foundword := IndexStr(words[i_currentword], words);
                IF (i_foundword > -1) AND (i_currentword <> i_foundword) THEN valid := false;
            END;
            IF valid THEN inc(answer);
        UNTIL eof(file_text);
        close(file_text);
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
