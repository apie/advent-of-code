const printMap = (lines: string[], pos: { x: number; y: number }): void => {
    lines.forEach((line, y) => {
        if (pos.y === y) {
            const lineArr = line.split("");
            if (line[pos.x] === "#") {
                lineArr[pos.x] = "X";
            } else {
                lineArr[pos.x] = "O";
            }
            console.log(lineArr.join(""));
        } else console.log(line);
    });
};
export const part1 = (lines: string[]): number => {
    const startPos = { x: 0, y: 0 };
    let pos = startPos;
    pos.x += 3;
    pos.y += 1;
    printMap(lines, pos);
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
