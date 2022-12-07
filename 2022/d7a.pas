PROGRAM d7a;
USES sysutils, classes, fgl;

	FUNCTION answer(filename:string) : int64;
	TYPE
		FStrucMap = specialize TFPGMap<string, TStringList>;
		FSizeMap = specialize TFPGMap<string, int64>;
	VAR
		filesystem_structure: FStrucMap;
		filesystem_size: FSizeMap;

		PROCEDURE parse_input;
		VAR
			f: text;
			l: string = '';
			curdir: TStringList;
			arg: string;
			s: string;
			p: integer;
			si: int64;
			parent: string;
			name: string;
		BEGIN
			answer := 0;
			curdir := TStringList.Create;
			filesystem_structure := FStrucMap.Create;
			filesystem_size := FSizeMap.Create;
			assign(f, filename);
			reset(f);
			REPEAT
				readln(f, l);
				IF l[1] = '$' THEN
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
				ELSE
				BEGIN
					p := pos(' ', l);
					s := copy(l, 1, p-1);
					name := copy(l, p+1);
					parent := curdir[curdir.Count-1];
					IF s = 'dir' THEN
					BEGIN
						IF filesystem_structure.IndexOf(parent) = -1 THEN filesystem_structure[parent] := TStringList.Create;
						filesystem_structure[parent].Add(name);
						si := 0;
					END
					ELSE si := strtoint(s);
					IF filesystem_size.IndexOf(parent) = -1 THEN filesystem_size[parent] := 0;
					filesystem_size[parent] := filesystem_size[parent] + si;
				END;
			UNTIL eof(f);
			close(f);
			curdir.Free;
		END;

	VAR
		i,j: integer;
		key: string;
		s: int64;
	BEGIN{answer}
		answer := 0;
		parse_input;

		writeln('xxxxxxxxx-structure-x');
		FOR i:=0 TO filesystem_structure.Count-1 DO
		BEGIN
			writeln('- ', filesystem_structure.Keys[i], ' ');
			FOR j:=0 TO filesystem_structure[filesystem_structure.Keys[i]].Count-1 DO
				writeln('  - ', filesystem_structure[filesystem_structure.Keys[i]][j], ' ');
			writeln();
		END;
		writeln('xxxxxxxxx-sizes-x');
		FOR i:=0 TO filesystem_size.Count-1 DO
		BEGIN
			key := filesystem_size.Keys[i];
			writeln(key, ' ', filesystem_size[key]);
		END;
		{Now we have per directory the size and per directory the location in the tree. We need to sum all the directories that are not in the root.}
{FIXME do this directly while parsing: on every ls, we can sum the dir and all the items in curdir. then we will be done in one pass!}
{FIXME test passes but answer is wrong, what about multiple nested dirs}
		writeln('xxxxxxxxx-summed for every dir all the underlying dirs-x');
		FOR i:=0 TO filesystem_structure.Count-1 DO
		BEGIN
			key := filesystem_structure.Keys[i];
			IF key = '/' THEN continue; {not interested}
			writeln(key, ' ');
			FOR j:=0 TO filesystem_structure[key].Count-1 DO
			BEGIN
				writeln('\ ', filesystem_structure[key][j], ' ');
				filesystem_size[key] := filesystem_size[key] + filesystem_size[filesystem_structure[key][j]];
			END;
			writeln();
		END;
		writeln();
		writeln('xxxxxxxxx-sizes incl subdir -x');
		FOR i:=0 TO filesystem_size.Count-1 DO
		BEGIN
			key := filesystem_size.Keys[i];
			s := filesystem_size[key];
			writeln(key, ' ', s);
			IF s <= 100000 THEN answer += s;
		END;
		filesystem_size.Free;
		filesystem_structure.Free;
	END;

CONST
    testfile1 = 'd7.test.1';
    testfile2 = 'd7.test.2';
    filename = 'd7.input';
VAR
    a: int64;
BEGIN{d7a}
    assert(answer(testfile1) = 95437, 'test 1 faal');
    assert(answer(testfile2) = 2, 'test 2 faal');
    a := answer(filename);
	assert(a > 977275);
    writeln('');
    writeln('answer: ', a);
END.
