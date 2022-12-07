PROGRAM d7a;
USES sysutils, classes, fgl;

	FUNCTION answer(filename:string) : longint;
	TYPE
{	fsrecord = RECORD size: longint; parent: string END;}
		FStrucMap = specialize TFPGMap<string, string>;
		FSizeMap = specialize TFPGMap<string, longint>;
	{
	  create above instance with
	  MClassMap := TMClassMap.Create;
	  somewhere and you can use it this way:
	  to put: MClassMap['strategy 1'] := TStrategyOneXX;
	  to get: SomeVar := MClassMap['strategy 1'];
	}
	VAR
		filesystem_structure: FStrucMap;
		filesystem_size: FSizeMap;
		f: text;
		l: string = '';
		curdir: TStringList;
		arg: string;
		i: integer;
{	curfile: fsrecord;}
		s: string;
		p: integer;
		si: longint;
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
			BEGIN
				CASE copy(l, 3, 2) OF
					'cd':
					BEGIN
						arg := copy(l, 6, length(l)-5);
{
						writeln('change directory');
						writeln(arg);
}
						IF arg = '..' THEN curdir.Delete(curdir.Count-1)
						ELSE IF arg = '/' THEN curdir.Add(trim(arg))
						ELSE curdir.Add('/'+trim(arg));
					END;
					'ls': ;
					ELSE writeln('unknown command!');
				END;
			END
			ELSE
			BEGIN
writeln('curdir:',curdir.Text);
{
				FOR i:=0 TO curdir.Count-1 DO write(curdir[i]);
				writeln();
				writeln(l);
}
				p := pos(' ', l);
				s := copy(l, 1, p-1);
				name := copy(l, p+1);
writeln('name:',name);
{
			writeln(p);
				writeln(s);
}
				parent := curdir[curdir.Count-1];
				IF s = 'dir' THEN
				BEGIN
					filesystem_structure[name] := parent;
					si := 0;
				END
				ELSE si := strtoint(s);
				writeln(parent, ', f  :', si, ';');
				IF filesystem_size.IndexOf(parent) = -1 THEN filesystem_size[parent] := 0;
				filesystem_size[parent] := filesystem_size[parent] + si;
				writeln(parent, ', tot:', filesystem_size[parent], ';');
			END;
		UNTIL eof(f);
		close(f);
		curdir.Free;

		writeln('xxxxxxxxx-structure-x');
		FOR i:=0 TO filesystem_structure.Count-1 DO writeln(filesystem_structure.Keys[i], ' ', filesystem_structure[filesystem_structure.Keys[i]]);
		writeln('xxxxxxxxx-sizes-x');
		FOR i:=0 TO filesystem_size.Count-1 DO writeln(filesystem_size.Keys[i], ' ', filesystem_size[filesystem_size.Keys[i]]);
		{Now we have per directory the size and per directory the location in the tree. We need to sum all the directories that are not in the root.}
		{TODO}
		{TODO now select only te

	END;

CONST
    testfile1 = 'd7.test.1';
    filename = 'd7.input';
VAR
    a: longint;
BEGIN{d7a}
    assert(answer(testfile1) = 95437, 'test 1 faal');
    a := answer(filename);
    writeln('');
    writeln('answer: ', a);
END.
