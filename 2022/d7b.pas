PROGRAM d7b;
USES sysutils, classes, fgl, math;
CONST
    FILESYSTEM_SIZE = 70000000;
    FREE_SPACE_NEEDED = 30000000;

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
        min_dir_size_needed,
        free_space: longint;
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
          {load list from delimited string} curdir.DelimitedText := d_string;
          WHILE curdir.count > 0 DO
          BEGIN
              d := curdir.DelimitedText;
              IF sizes.IndexOf(d) = -1 THEN sizes[d] := 0;
              sizes[d] := sizes[d] + size;
              {go up one dir} curdir.Delete(curdir.Count-1);
            END;
        END;

        free_space := FILESYSTEM_SIZE - sizes['"/"'];
        writeln('current free space ', free_space);
        min_dir_size_needed := FREE_SPACE_NEEDED - free_space;
        writeln('need to free additional ', min_dir_size_needed);

		answer := FILESYSTEM_SIZE;
        FOR i:=0 TO sizes.Count-1 DO
            IF sizes.data[i] >= min_dir_size_needed THEN
                answer := min(answer, sizes.data[i]);

        files.Free();
        sizes.Free();
        curdir.Free();
	END;

CONST
    testfile1 = 'd7.test.1';
    filename = 'd7.input';
VAR
    a: longint;
BEGIN{d7b}
    assert(answer(testfile1) = 24933642, 'test 1 faal');
    a := answer(filename);
    writeln('');
    writeln('answer: ', a);
END.
