PROGRAM d2a;

FUNCTION answer(filename:string) : integer;
TYPE
    guide_line = array[1..3] of char;

    FUNCTION score(guide_l:guide_line) : integer;
    CONST
        YOU_ROCK = 'X';
        YOU_PAPER = 'Y';
        YOU_SCISSORS = 'Z';
        OPPONENT_ROCK = 'A';
        OPPONENT_PAPER = 'B';
        OPPONENT_SCISSORS = 'C';
    BEGIN
        score := 0;
        {Score of the shape you selected}
        IF guide_l[3] = YOU_ROCK THEN score += 1
        ELSE IF guide_l[3] = YOU_PAPER THEN score += 2
        ELSE IF guide_l[3] = YOU_SCISSORS THEN score += 3;
        {Plus the score for the outcome of the round}
        {0 if you lost, 3 if draw, 6 if you won}
        IF (guide_l[3] = YOU_ROCK) AND (guide_l[1] = OPPONENT_ROCK) THEN score += 3
        ELSE IF (guide_l[3] = YOU_ROCK) AND (guide_l[1] = OPPONENT_PAPER) THEN score += 0
        ELSE IF (guide_l[3] = YOU_ROCK) AND (guide_l[1] = OPPONENT_SCISSORS) THEN score += 6
        ELSE IF (guide_l[3] = YOU_PAPER) AND (guide_l[1] = OPPONENT_ROCK) THEN score += 6
        ELSE IF (guide_l[3] = YOU_PAPER) AND (guide_l[1] = OPPONENT_PAPER) THEN score += 3
        ELSE IF (guide_l[3] = YOU_PAPER) AND (guide_l[1] = OPPONENT_SCISSORS) THEN score += 0
        ELSE IF (guide_l[3] = YOU_SCISSORS) AND (guide_l[1] = OPPONENT_ROCK) THEN score += 0
        ELSE IF (guide_l[3] = YOU_SCISSORS) AND (guide_l[1] = OPPONENT_PAPER) THEN score += 6
        ELSE IF (guide_l[3] = YOU_SCISSORS) AND (guide_l[1] = OPPONENT_SCISSORS) THEN score += 3;
    END;
VAR
    f: text;
    guide: ARRAY[1..2500] OF guide_line;
    i: integer;
    totscore: integer = 0;
BEGIN
    assign(f, filename);
    reset(f);
    i := 1;
    WHILE not eof(f) DO
    BEGIN
        readln(f, guide[i]);
        i :=+ 1;
        totscore += score(guide[i]);
    END;
    close(f);
    answer := totscore;
END;

CONST
    testfile = 'd2.test.1';
    filename = 'd2.input';
VAR
    a : integer;
BEGIN{d2a}
    assert(answer(testfile) = 15, 'test faal');
    a := answer(filename);
    writeln('');
    writeln('answer: ', a);
    writeln('klaar');
END.
