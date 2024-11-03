const printMap2 = (
    lines: string[],
    positions: { x: number; y: number }[],
): number => {
    let numTreesEncountered = 0
    lines.forEach((line, y) => {
        let lineArr = line.split("");
        const pos = positions[y-1];
        // console.log(pos)
        if (!pos) return;
        while (positions[positions.length-1].x > lineArr.length) {
            lineArr = lineArr.concat(lineArr);
        }
        if (pos.y === y) {
            if (lineArr[pos.x] === "#") {
                lineArr[pos.x] = "X";
                numTreesEncountered += 1;
            } else {
                lineArr[pos.x] = "O";
            }
            console.log(lineArr.join(""));
        } else console.log(lineArr.join(""));
    });
    console.log();
    return numTreesEncountered
};
export const part1 = (lines: string[]): number => {
    const startPos = { x: 0, y: 0 };
    const pos = startPos;
    const positions: { x: number; y: number }[] = [];
    while (pos.y < lines.length - 1) {
        pos.x += 3;
        pos.y += 1;
        positions[positions.length] = { ...pos };
        // printMap(lines, pos);
    }
    console.log(positions);
    return printMap2(lines, positions);
};
export const part2 = (lines: string[]): number => {
    return 0;
};

function d03(input: string): number[] {
    const lines = input.trim().split("\n");
    return [
        part1(lines),
        part2(lines),
    ];
}

export default d03;
