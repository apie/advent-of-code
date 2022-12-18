PROGRAM d17a;
USES sysutils, classes, fgl, strutils;
TYPE
    rockIndex = 0..4;
CONST
    cavewidth = 7;
    maxrockheight = 4;
    maxrockwidth = 4;
    emptyrow = '.......';
    nrocks = 5;
    rock1 = '@@@@............';{rock layout without linebreaks}
    rock2 = '.@..@@@..@......';
    rock3 = '..@...@.@@@.....';
    rock4 = '@...@...@...@...';
    rock5 = '@@..@@..........';
VAR
    rocks : array [low(rockindex)..high(rockindex)] of array[1..maxrockwidth*maxrockheight] of char = (rock1, rock2, rock3, rock4, rock5);


	FUNCTION answer(filename:string) : longint;
	VAR
        currentRock: rockIndex = nrocks-1;{set at last rock since we shift rock right at the start and will then end up with rock1}
        rockheight : array[rockindex] of integer = (1, 3, 3, 4, 2);
        cave: TStringList;
        newRockCalled : integer = 0;

        PROCEDURE printCave();
        VAR
            i : integer;
        BEGIN
        if true then begin
            writeln();
            FOR i:=cave.Count-1 DOWNTO 1 DO writeln('|',cave[i],'|');
            writeln('+-------+');
        END;
        END;

        PROCEDURE addNewRock();
        var
            i : integer;
            row: array[1..cavewidth] of char;
        BEGIN
            inc(newRockCalled);
            writeln('A new rock begins falling:');
            currentRock := (currentRock +1) mod nrocks;
            cave.Add(emptyrow); cave.Add(emptyrow); cave.Add(emptyrow);
            for i:=rockheight[currentRock] downto 1 do
            begin
                row := '..'+copy(rocks[currentRock], (i-1)*maxrockheight+1, maxrockwidth)+'.';
                cave.add(row);
            end;
            printcave;
        END;

        PROCEDURE moveRock(direction: char);
        VAR
            dir : integer = 1;
            edgerock, i : integer;
            nothingOnSides : boolean = false;
            onedge : boolean = false;
            lrfree : boolean = false;
            row: array[1..cavewidth] of char;
        BEGIN
            IF direction = '<' THEN dir := -1;
            writeln('moving rock ', dir);
            FOR i:=cave.Count-1 DOWNTO cave.Count-1-rockheight[currentrock] DO
            IF i > 0 THEN
            BEGIN
                IF (dir > 0) AND (cave[i][cavewidth] = '@') THEN onedge := true;
                IF (dir < 0) AND (cave[i][1        ] = '@') THEN onedge := true;
            END;
            writeln('onedge ', onedge);
            IF not onedge THEN
            BEGIN
                {shortcut. check if nothing on the sides}
                nothingOnSides := true;
                FOR i:=cave.Count-1 DOWNTO cave.Count-1-rockheight[currentrock]-1 DO
                    IF (i > 0) AND (pos('#', cave[i]) > 0) THEN nothingOnSides := false;
                {move}
                IF nothingOnSides THEN
                BEGIN
                    FOR i:=cave.Count-1 DOWNTO cave.Count-1-rockheight[currentrock] DO
                    IF i > 0 THEN
                        IF (dir > 0) THEN cave[i] := '.'+copy(cave[i], 1, cavewidth-1)
                        ELSE cave[i] := copy(cave[i], 2, cavewidth)+'.';
                END;
                IF not nothingOnSides THEN
                BEGIN
                    if (dir > 0) then
                    begin
                        {move right, check if right side is free along the height of the cave}
                        lrfree := true;
                        FOR i:=cave.Count-1 DOWNTO 1 DO
                        IF (i>0) THEN
                        BEGIN
                            edgeRock := rpos('@', cave[i]);
                            IF (edgeRock > 0) AND (cave[i][edgeRock+1] <> '.') THEN lrfree := false;
                        end;
                        IF lrfree THEN FOR i:=cave.Count-1 DOWNTO 1 DO
                        IF (i>0) THEN
                        BEGIN
                            edgeRock := rpos('@', cave[i]);
                            if (edgeRock > 0) THEN
                            BEGIN
                                row := cave[i];
                                row[edgeRock+1] := '@';{paint right side}
                                edgeRock := pos('@', cave[i]);
                                row[edgeRock] := '.';{paint left side}
                                cave[i] := row;
                            END;
                        end;
                    end
                    else
                    begin
                        {move left, check if left side is free along the height of the cave}
                        lrfree := true;
                        FOR i:=cave.Count-1 DOWNTO 1 DO
                        IF (i>0) THEN
                        BEGIN
                            edgeRock := pos('@', cave[i]);
                            IF (edgeRock > 0) AND (cave[i][edgeRock-1] <> '.') THEN lrfree := false;
                        end;
                        IF lrfree THEN FOR i:=cave.Count-1 DOWNTO 1 DO
                        IF (i>0) THEN
                        BEGIN
                            edgeRock := rpos('@', cave[i]);
                            if (edgeRock > 0) THEN
                            BEGIN
                                row := cave[i];
                                row[edgeRock] := '.';{paint right side}
                                edgeRock := pos('@', cave[i]);
                                row[edgeRock-1] := '@';{paint left side}
                                cave[i] := row;
                            end;
                        end;
                    end;

                END;
            END;
        END;

        FUNCTION cameToRest : boolean;
        VAR
            i,j : integer;
        BEGIN
            cameToRest := false;
            FOR j := 1 to cavewidth DO 
            FOR i:=cave.Count-1 DOWNTO 1 DO{go all the way down, could have a hight tower}
            {if we have an @, check just below it if there is an #, if so, it came to rest.}
                IF (cave[i][j] = '@') and (cave[i-1][j] = '#') THEN cameToRest := true;
        END;

        PROCEDURE freezeIt;
        VAR
            i,j : integer;
            row: array[1..cavewidth] of char;
        BEGIN
            {if rock came to rest, als dat zo is dan @ vervangen door #}
            FOR i:=cave.Count-1 DOWNTO 1 DO{go all the way down, could have a hight tower}
                if i>0 then
                    FOR j := 1 to cavewidth DO 
                        IF (cave[i][j] = '@') then
                        BEGIN
                            row := cave[i];
                            row[j] := '#';
                            cave[i] := row;
                        END;
        END;

        FUNCTION letItFall : boolean;
        VAR
            i,j,k, colFound, belowFound : integer;
            fallIdx : integer = -1;
            row: array[1..cavewidth] of char;
        BEGIN
            letItFall := false;
            writeln('Rock falls 1 unit');
            IF cameToRest then
            BEGIN
                freezeIt;
                letItFall := true;
            END
            ELSE
            BEGIN
                {shortcut. check if empty row just beneath rock}
                FOR i:=cave.Count-1 DOWNTO cave.Count-1-rockheight[currentrock]-1 DO
                    IF (i > 0) AND (cave[i] = emptyrow) THEN fallIdx := i;
                IF fallIdx <> -1 THEN cave.Delete(fallIdx)
                ELSE
                BEGIN
                    FOR j:=1 TO cavewidth DO
                    FOR i:=cave.Count-1 DOWNTO 1 DO{go all the way down, could have a hight tower}
                    BEGIN
                        {only once per col, find top of rock}
                        IF (cave[i][j] = '@') THEN
                        BEGIN
                            {check if empty space below rock. then we move it down}
                            FOR k:=i DOWNTO 1 DO
                            IF (cave[k][j] = '.') THEN
                            BEGIN
                                row := cave[k];
                                row[j] := '@';
                                cave[k] := row;
                                break;
                            END;

                            {change top to dots}
                            row := cave[i];
                            row[j] := '.';
                            cave[i] := row;
                            break;
                        END;
                    END;
                END;
            END;
            {remove any empty rows on the top that have now occured}
            IF (cave[cave.Count-1] = emptyrow) THEN cave.Delete(cave.Count-1);
            printcave;
        END;

	VAR
        f: text;
        c: char;
        rockCameToRest : boolean = false;
        i:integer = 0;
        key : char;
        row: array[1..cavewidth] of char;
    BEGIN{answer}
		answer := 0;
        cave := TStringList.Create;
        row := '#######';
        cave.Add(row);
        addNewRock();
        assign(f, filename);
        reset(f);
        REPEAT
            writeln();
            if eof(f) THEN reset(f);
            read(f, c);
            moveRock(c);
            printcave;
            rockCameToRest := letItFall;
            IF rockCameToRest and (newRockCalled < 2022) THEN addNewRock();
            read(key);
            writeln('New rocks: ', newRockCalled, '. Cave height: ', cave.Count);
        UNTIL (newRockCalled >= 2022) OR (key='q');
        close(f);
        answer := cave.Count;
        writeln(answer);
        cave.Free;
	END;

VAR
    a: longint;
BEGIN{d17a}
    assert(answer('d17.test.1') = 3068, 'test 1 faal');
    a := answer('d17.input');
    writeln('');
    writeln('answer: ', a);
END.
