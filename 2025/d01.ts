import "./util.ts";
import { p } from "./util.ts";

export const part1 = (lines: string[]): number => {
    console.log(
        "Part 1: the number of times the dial is left pointing at 0 after any rotation in the sequence.",
    );
    let pos = 50;
    return lines.map((line) => {
        const direction = line[0];
        const amount = parseInt(line.substring(1));
        p("Instructions:", direction, amount);
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
        p("Pos:", pos);
        return (pos % 100 === 0);
    }).sum();
};
export const part2 = (lines: string[]): number => {
    console.log(
        "Part 2: the number of times the dial passes or lands on 0.",
    );
    const { pos, passedZero } = lines.reduce(({ pos, passedZero }, line) => {
        p("Pos:", pos);
        const direction = line[0];
        const amount = parseInt(line.substring(1).trim());
        p("Instructions:", direction, amount);
        let dir;
        switch (direction) {
            case "L":
                dir = -1;
                break;
            case "R":
                dir = 1;
                break;
            default:
                throw Error("Unknown direction");
        }
        for (
            let remainingAmount = amount;
            remainingAmount > 0;
            remainingAmount--
        ) {
            pos += dir;
            if (pos % 100 === 0) {
                passedZero++;
                p("---passed zero!");
            }
        }
        return { pos: pos, passedZero: passedZero };
    }, { pos: 50, passedZero: 0 });
    p("pos", pos, "passedzero", passedZero);
    return passedZero;
};

function* d01(input: string): Generator<number> {
    console.log("Day 1: Secret entrance");
    const lines = input.trim().split("\n");
    yield part1(lines);
    yield part2(lines);
}

export default d01;
