import "./util.ts";
import { p } from "./util.ts";

const idInvalid = (id: number): boolean => {
    const result = id.toString().match(/^(\d+?)\1$/);
    const invalid = !!result;
    // if(invalid) p("is invalid?", id, invalid, result);
    return invalid;
};
const getIds = (range: string): number[] => {
    p("range:", range);
    const [start, end] = range.split("-").map((s) => Number(s));
    // p(start, end);
    const ids = [];
    for (let i = start; i <= end; i++) ids.push(i);
    return ids;
};
const sumOfInvalidIds = (line: string): number => {
    return line.split(",").map((range) =>
        getIds(range).map((id) => idInvalid(id) ? id : 0).sum()
    ).sum();
};
export const part1 = (lines: string[]): number => {
    console.log("Part 1: Get the sum of the invalid ids.");
    return sumOfInvalidIds(lines[0]);
};
export const part2 = (lines: string[]): number => {
    return 0;
};

function* d02(input: string): Generator<number> {
    console.log("Day 2: Gift Shop");
    const lines = input.trim().split("\n");
    yield part1(lines);
    yield part2(lines);
}

export default d02;
