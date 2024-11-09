import { assert } from "jsr:@std/assert/assert";
import "./util.ts";
const countYes = (group: string): number => {
    const uniqueChars = new Set(group.replaceAll("\n", ""));
    console.log(group);
    console.log(uniqueChars);
    return uniqueChars.size;
};
export const part1 = (groups: string[]): number => {
    console.log(groups);
    const answer = groups.map((group) => countYes(group)).sum();
    assert(answer < 6715, "too high");
    return answer;
};
export const part2 = (lines: string[]): number => {
    return 0;
};

function d06(input: string): number[] {
    const lines = input.trim().split("\n\n");
    return [
        part1(lines),
        part2(lines),
    ];
}

export default d06;
