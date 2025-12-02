import "./util.ts";
import { p } from "./util.ts";

const idInvalid = (id: number): boolean => {
    const result = id.toString().match(/^(\d+?)\1$/);
    const invalid = !!result;
    if (invalid) p("is invalid", id);
    return invalid;
};
const idInvalid2 = (id: number): boolean => {
    const result = id.toString().match(/^(\d+?)\1+$/);
    const invalid = !!result;
    if (invalid) p("is invalid2", id);
    return invalid;
};
const getIds = (range: string): number[] => {
    p("range:", range);
    const [start, end] = range.split("-").map((s) => Number(s));
    const ids = [];
    for (let i = start; i <= end; i++) ids.push(i);
    return ids;
};
const sumOfInvalidIds = (line: string): number => {
    return line.split(",").map((range) =>
        getIds(range).map((id) => idInvalid(id) ? id : 0).sum()
    ).sum();
};
const sumOfInvalidIds2 = (line: string): number => {
    return line.split(",").map((range) =>
        getIds(range).map((id) => idInvalid2(id) ? id : 0).sum()
    ).sum();
};
export const part1 = (lines: string[]): number => {
    console.log("Part 1: Get the sum of the invalid ids.");
    return sumOfInvalidIds(lines[0]);
};
export const part2 = (lines: string[]): number => {
    console.log(
        "Part 2: Get the sum of the invalid ids that appear at least twice.",
    );
    return sumOfInvalidIds2(lines[0]);
};

function* d02(input: string): Generator<number> {
    console.log("Day 2: Gift Shop");
    const lines = input.trim().split("\n");
    yield part1(lines);
    yield part2(lines);
}

export default d02;
