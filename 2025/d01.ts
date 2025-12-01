import "./util.ts";
import { p } from "./util.ts";

export const part1 = (lines: string[]): number => {
    console.log(
        "Part 1: the number of times the dial is left pointing at 0 after any rotation in the sequence.",
    );
    let pos = 50;
    p("pos:", pos);
    return lines.map((line) => {
        const direction = line[0];
        const amount = parseInt(line.substring(1));
        p(direction, amount);
        switch (direction) {
            case "L":
                pos -= amount;
                break;
            case "R":
                pos += amount;
                break;
            default:
                throw Error("Unknown direction");
        }
        while (pos < 0) pos += 100;
        while (pos > 99) pos -= 100;
        p("pos:", pos);
        if (pos === 0) return 1;
        return 0;
    }).sum();
};
export const part2 = (lines: string[]): number => {
    return 0;
};

function* d01(input: string): Generator<number> {
    console.log("Day 1: Secret entrance");
    const lines = input.trim().split("\n");
    yield part1(lines);
    yield part2(lines);
}

export default d01;
