PROGRAM d7a;
USES sysutils, classes, fgl;

	FUNCTION answer(filename:string) : int64;
	TYPE
		FSizeMap = specialize TFPGMap<string, int64>;
	VAR
		sizes: FSizeMap;

		PROCEDURE parse_input;
		VAR
			curdir: TStringList;
			f: text;
			l: string;
			arg: string;
			sizecol: string;
			i: integer;
			size: int64;
			dirname: string;
		BEGIN
			curdir := TStringList.Create;
			sizes := FSizeMap.Create;
			assign(f, filename);
			reset(f);
			REPEAT
				readln(f, l);
				IF l[1] = '$' THEN{a command}
					CASE copy(l, 3, 2) OF
						'cd':
						BEGIN
							arg := copy(l, 6, length(l)-5);
							IF arg = '..' THEN curdir.Delete(curdir.Count-1)
							ELSE curdir.Add(trim(arg));
						END;
						'ls': ;
						ELSE writeln('unknown command!');
					END
				ELSE {not a command. ls-output}
				BEGIN
					sizecol := copy(l, 1, pos(' ', l)-1);
					IF sizecol = 'dir' THEN size := 0
					ELSE size := strtoint64(sizecol);

                    {we can add this size to the current dir and all the dirs above it}
                    FOR i:= 0 TO curdir.Count-1 DO
                    BEGIN
                        dirname := curdir[i];
                        IF sizes.IndexOf(dirname) = -1 THEN sizes[dirname] := 0;
                        sizes[dirname] := sizes[dirname] + size;
                    END;
				END;
			UNTIL eof(f);
			close(f);
			curdir.Free();
		END;

	VAR
		i: integer;
		key: string;
		size: int64;
	BEGIN{answer}
		answer := 0;
		parse_input;

		writeln('*********** sizes');
		FOR i:=0 TO sizes.Count-1 DO BEGIN
			key := sizes.Keys[i];
			size := sizes[key];
			IF size <= 100000 THEN BEGIN
                answer += size;
                writeln(answer, ' ', key, ' ', size);
            END;
		END;
		sizes.Free();
	END;

CONST
    testfile1 = 'd7.test.1';
    testfile2 = 'd7.test.2';
    filename = 'd7.input';
VAR
    a: int64;
BEGIN{d7a}
    assert(answer(testfile1) = 95437, 'test 1 faal');
    assert(answer(testfile2) = 3, 'test 2 faal');
    a := answer(filename);
	assert(a > 977275);
	assert(a > 1072909);
    writeln('');
    writeln('answer: ', a);
END.
