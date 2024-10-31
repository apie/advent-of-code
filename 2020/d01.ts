import { combinations2, combinations3, prod, sum } from "./util.ts";

export const solution = (combs: Generator<number[]>): number => {
    const a = combs.find((c) => sum(c) == 2020);
    if (!a) throw Error;
    return prod(a);
};

export const part1 = (lines: number[]): number => {
    const combs = combinations2(lines, lines);
    return solution(combs)
};
export const part2 = (lines: number[]): number => {
    const combs = combinations3(lines, lines, lines);
    return solution(combs)
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
