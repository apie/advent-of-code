const printMap = (lines: string[], pos: { x: number; y: number }): void => {
    lines.forEach((line, y) => {
        let lineArr = line.split("");
        while (pos.x > lineArr.length) {
            lineArr = lineArr.concat(lineArr);
        }
        if (pos.y === y) {
            if (lineArr[pos.x] === "#") {
                lineArr[pos.x] = "X";
            } else {
                lineArr[pos.x] = "O";
            }
            console.log(lineArr.join(""));
        } else console.log(lineArr.join(""));
    });
    console.log();
};
export const part1 = (lines: string[]): number => {
    const startPos = { x: 0, y: 0 };
    const pos = startPos;
    while (pos.y < lines.length -1) {
        pos.x += 3;
        pos.y += 1;
        printMap(lines, pos);
    }
    return 0;
};
export const part2 = (lines: string[]): number => {
    return 0;
};

function d01(input: string): number[] {
    const lines = input.trim().split("\n");
    return [
        part1(lines),
        part2(lines),
    ];
}

export default d01;
