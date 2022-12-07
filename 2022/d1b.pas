PROGRAM d1b;
USES sysutils, integerlist;
TYPE
    longintlist= TInt64List;

    FUNCTION answer(filename:string) : longint;

    VAR
        f: text;
        l: string;
        elf_total_calories: longint = 0;
        i: integer;
        highest: longintlist;
    BEGIN
        answer := 0;
        highest := longintlist.Create;
        assign(f, filename);
        reset(f);
        REPEAT
            readln(f, l);
            IF l <> '' THEN elf_total_calories += strtoint(l)
            ELSE
            BEGIN{next elf}
                highest.Add(elf_total_calories);
                elf_total_calories := 0;
                continue;
            END;
        UNTIL eof(f);
        highest.Add(elf_total_calories);
        close(f);
        highest.Sort;
        FOR i:=highest.Count-3 TO highest.Count-1 DO answer += highest[i];
    END;

CONST
    testfile = 'd1.test.1';
    filename = 'd1.input';
BEGIN{d1b}
    assert(answer(testfile) = 45000, 'test faal');
    writeln('answer: ', answer(filename));
END.
