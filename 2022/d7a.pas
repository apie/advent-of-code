PROGRAM d7a;
USES sysutils, classes, fgl;

	FUNCTION answer(filename:string) : longint;
	TYPE
		FSizeMap = specialize TFPGMap<string, longint>;
	VAR
        files: TStringList;
        sizes: FSizeMap;

		PROCEDURE parse_input;
		VAR
			curdir: TStringList;
			f: text;
			l: string;
			arg: string;
			sizecol: string;
		BEGIN
			curdir := TStringList.Create;
            curdir.delimiter := '/';
			assign(f, filename);
			reset(f);
            readln(f, l); {eat first line since we dont need it}
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
					END
				ELSE {not a command. ls-output}
				BEGIN
					sizecol := copy(l, 1, pos(' ', l)-1);
					IF sizecol <> 'dir' THEN files.add(curdir.DelimitedText + ',' + l); 
				END;
			UNTIL eof(f);
			close(f);
			curdir.Free();
		END;

	VAR
        f: string;
        d_string: string;
        d: string;
        size: longint;
        i: integer;
        curdir: TStringList;
	BEGIN{answer}
        files := TStringList.Create;
        sizes := FSizeMap.Create;
		parse_input();
        curdir := TStringList.Create;
        curdir.delimiter := '/';

        FOR f IN files DO
        BEGIN
          d_string := copy(f, 1, pos(',', f)-1);
          size := strToInt64(copy(f, pos(',', f)+1, pos(' ', f)-pos(',', f)-1));
          curdir.DelimitedText := d_string;
          WHILE curdir.count > 0 DO
          BEGIN
              d := curdir.DelimitedText;
              IF sizes.IndexOf(d) = -1 THEN sizes[d] := 0;
              sizes[d] := sizes[d] + size;
              {go up one dir} curdir.Delete(curdir.Count-1);
            END;
        END;

		answer := 0;
        FOR i:=0 TO sizes.Count-1 DO
        BEGIN
          IF sizes.data[i] > 100000 THEN continue;
          answer += sizes.data[i];
        END;

        files.Free();
        sizes.Free();
        curdir.Free();
	END;

CONST
    testfile1 = 'd7.test.1';
    testfile2 = 'd7.test.2';
    filename = 'd7.input';
VAR
    a: longint;
BEGIN{d7a}
    assert(answer(testfile1) = 95437, 'test 1 faal');
    assert(answer(testfile2) = 2, 'test 2 faal');
    a := answer(filename);
	assert(a > 977275);
	assert(a <> 1072909);
	assert(a <> 1829781);
    writeln('');
    writeln('answer: ', a);
END.
