import { combinations } from "./util.ts";

export const part1 = (lines: number[]): number => {
    const combs = combinations(lines, lines);
    const a = combs.find(([a, b]) => a + b == 2020);
    if (!a) throw Error;
    return a[0] * a[1];
};
export const part2 = (lines: number[]): number => {
    return 0;
};

function d01(input: string): number[] {
    const lines = input.trim().split("\n").filter((line) => line.match(/^\d/))
        .map((line) => Number(line));
    return [
        part1(lines),
        part2(lines),
    ];
}

export default d01;
