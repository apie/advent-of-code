import "./util.ts";

type Slope = { x: number; y: number };
type Position = { x: number; y: number };

const printMapAndCountTrees = (
    lines: string[],
    positions: Position[],
): number => {
    const mapWidth = positions[positions.length - 1].x;
    let numTreesEncountered = 0;
    lines.forEach((line, y) => {
        // consider first pos
        const pos = positions[0];
        if (!pos) return;
        let lineArr = line.split("");
        while (mapWidth > lineArr.length) {
            lineArr = lineArr.concat(lineArr);
        }
        if (pos.y === y) {
            // arrived at the row of the first pos, so consider it handled
            positions.shift();
            if (lineArr[pos.x] === "#") {
                lineArr[pos.x] = "X";
                numTreesEncountered += 1;
            } else {
                lineArr[pos.x] = "O";
            }
        }
        // just print the line
        console.log(lineArr.join(""));
    });
    console.log();
    return numTreesEncountered;
};
const traverseMap = (
    slope: Slope,
    maxLines: number,
): Position[] => {
    const startPos: Position = { x: 0, y: 0 };
    const pos = startPos;
    const positions: Position[] = [];
    while (pos.y < maxLines - 1) {
        pos.x += slope.x;
        pos.y += slope.y;
        positions[positions.length] = { ...pos };
    }
    return positions;
};
const getTreesOnMap = (
    cave: string[],
    slope: Slope,
): number => {
    console.log(`-------SLOPE: ${slope.x} ${slope.y} -----------`);
    const positions = traverseMap(slope, cave.length);
    return printMapAndCountTrees(cave, positions);
};

export const part1 = (lines: string[]): number => {
    return getTreesOnMap(lines, { x: 3, y: 1 });
};
export const part2 = (lines: string[]): number => {
    return [
        { x: 1, y: 1 },
        { x: 3, y: 1 },
        { x: 5, y: 1 },
        { x: 7, y: 1 },
        { x: 1, y: 2 },
    ].map((slope) => getTreesOnMap(lines, slope)).prod();
};

function d03(input: string): number[] {
    const lines = input.trim().split("\n");
    return [
        part1(lines),
        part2(lines),
    ];
}

export default d03;
