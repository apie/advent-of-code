import { assert } from "jsr:@std/assert/assert";
import "./util.ts";

const getLists = (lines: string[]): { first: number[]; second: number[] } => {
    const first = lines.map((line) => Number(line.split("   ")[0]));
    const second = lines.map((line) => Number(line.split("   ")[1]));
    assert(first.length === second.length);
    return { "first": first, "second": second };
};
export const part1 = (lines: string[]): number => {
    let { first, second } = getLists(lines);
    first = first.sort();
    second = second.sort();
    return first.map((fitem, i) => [fitem, second[i]]).map((
        [pairl, pairr],
    ) => Math.abs(pairl - pairr)).sum();
};
export const part2 = (lines: string[]): number => {
    const { first, second } = getLists(lines);
    const countz = first.map((fitem) => [fitem, second.count(fitem)]);
    const scores = countz.map(([num, num_appear]) => num * num_appear);
    return scores.sum();
};

function d01(input: string): number[] {
    const lines = input.trim().split("\n");
    return [
        part1(lines),
        part2(lines),
    ];
}

export default d01;
