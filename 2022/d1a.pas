PROGRAM d1a;
USES sysutils;

    FUNCTION answer(filename:string) : longint;
    VAR
        f: text;
        l: string;
        elf_total_calories: longint = 0;
    BEGIN
        answer := 0;
        assign(f, filename);
        reset(f);
        REPEAT
            readln(f, l);
            IF l <> '' THEN elf_total_calories += strtoint(l)
            ELSE
            BEGIN{next elf}
                IF elf_total_calories > answer THEN answer := elf_total_calories;
                elf_total_calories := 0;
                continue;
            END;
        UNTIL eof(f);
        IF elf_total_calories > answer THEN answer := elf_total_calories;
        close(f);
    END;

CONST
    testfile = 'd1.test.1';
    filename = 'd1.input';
BEGIN{d1a}
    assert(answer(testfile) = 24000, 'test faal');
    writeln('answer: ', answer(filename));
END.
