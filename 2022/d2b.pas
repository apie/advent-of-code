PROGRAM d2b;

FUNCTION answer(filename:string) : integer;
TYPE
    guide_line = array[1..3] of char;

    FUNCTION score(guide_l:guide_line) : integer;
    CONST
        YOU_ROCK = 'X';
        YOU_PAPER = 'Y';
        YOU_SCISSORS = 'Z';
        YOU_LOSE = 'X';
        YOU_DRAW = 'Y';
        YOU_WIN = 'Z';
        OPPONENT_ROCK = 'A';
        OPPONENT_PAPER = 'B';
        OPPONENT_SCISSORS = 'C';
    VAR
        your_shape : char;
    BEGIN
        score := 0;
        {0 if you lost, 3 if draw, 6 if you won}
        {Find out what you need to play to get the desired outcome}
        CASE guide_l[3] OF
            YOU_LOSE:
                BEGIN
                    score += 0;
                    CASE guide_l[1] OF
                        OPPONENT_ROCK: your_shape := YOU_SCISSORS;
                        OPPONENT_PAPER: your_shape := YOU_ROCK;
                        OPPONENT_SCISSORS: your_shape := YOU_PAPER;
                    END;
                END;
            YOU_DRAW:
                BEGIN
                    score += 3;
                    CASE guide_l[1] OF
                        OPPONENT_ROCK: your_shape := YOU_ROCK;
                        OPPONENT_PAPER: your_shape := YOU_PAPER;
                        OPPONENT_SCISSORS: your_shape := YOU_SCISSORS;
                    END;
                END;
            YOU_WIN:
                BEGIN
                    score += 6;
                    CASE guide_l[1] OF
                        OPPONENT_ROCK: your_shape := YOU_PAPER;
                        OPPONENT_PAPER: your_shape := YOU_SCISSORS;
                        OPPONENT_SCISSORS: your_shape := YOU_ROCK;
                    END;
                END;
        END;
        {plus Score of the shape you selected}
        CASE your_shape OF
            YOU_ROCK: score += 1;
            YOU_PAPER: score += 2;
            YOU_SCISSORS: score += 3;
        END;
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
BEGIN{d2b}
    assert(answer(testfile) = 12, 'test faal');
    a := answer(filename);
    writeln('');
    writeln('answer: ', a);
    writeln('klaar');
END.
