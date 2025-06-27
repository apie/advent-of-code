import "./util.ts";
import { p } from "./util.ts";

export const part1 = (lines: string[]): number => {
    return 0;
};
export const part2 = (lines: string[]): number => {
    return 0;
};

function* d_DAY_(input: string): Generator<number> {
    const lines = input.trim().split("\n");
    yield part1(lines);
    yield part2(lines);
}

export default d_DAY_;
