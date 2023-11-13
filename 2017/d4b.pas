PROGRAM d4b;
USES sysutils, strutils;

    FUNCTION anagram(const s1, s2:string) : boolean;
    VAR
        t1, t2: string;
        i_t1char_in_t2,
        i_currentchar_t1: integer;
    BEGIN
        anagram := false;
        IF length(s1) = length(s2) THEN
        BEGIN
            t1 := s1;
            t2 := s2;
            FOR i_currentchar_t1:=1 TO length(t1) DO
            BEGIN
                i_t1char_in_t2 := pos(t1[i_currentchar_t1], t2);
                {check each char of t1. if it appears in t2. mark the chars in t1 and t2.}
                IF i_t1char_in_t2 > 0 THEN
                BEGIN
                    t1[i_currentchar_t1] := '.';
                    t2[i_t1char_in_t2] := '.';
                END;
            END;
            IF t1 = t2 THEN anagram := true;
        END;
    END;

    FUNCTION answer(filename:string) : longint;
    VAR
        file_text: text;
        line_s: string;
        words: TStringArray;
        i_currentword, j_currentword: integer;
        valid: boolean;
    BEGIN{answer}
        answer := 0;
        assign(file_text, filename);
        reset(file_text);
        REPEAT
            readln(file_text, line_s);
            line_s := trim(line_s);
            words := SplitString(line_s, ' ');
            valid := true;
            FOR i_currentword:=0 TO length(words)-1 DO
                FOR j_currentword:=0 TO length(words)-1 DO
                    IF i_currentword<>j_currentword THEN
                        IF anagram(words[i_currentword], words[j_currentword]) THEN valid := false;
            IF valid THEN inc(answer);
        UNTIL eof(file_text);
        close(file_text);
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
