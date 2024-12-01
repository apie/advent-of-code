import { assert } from "jsr:@std/assert/assert";
import "./util.ts";

export const part1 = (lines: string[]): number => {
    // console.log(lines)
    const first = lines.map((line) => Number(line.split("   ")[0])).sort();
    const second = lines.map((line) => Number(line.split("   ")[1])).sort();
    console.log(first);
    console.log(second);
    assert(first.length === second.length);
    const ans = first.map((fitem, i) => [fitem, second[i]]).map((
        [pairl, pairr],
    ) => Math.abs(pairl - pairr)).sum();
    console.log(ans);
    return ans;
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
