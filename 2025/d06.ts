import "./util.ts";
import { p } from "./util.ts";

const getColTot = (parsed: string[][], col: number): number => {
    let coltot = 0;
    const sub: number[] = [];
    for (let row = 0; row < parsed.length - 1; row++) {
        // p(parsed[row][col]);
        sub.push(Number(parsed[row][col]));
    }
    switch (parsed[parsed.length - 1][col]) {
        case "*":
            coltot = sub.prod();
            break;
        case "+":
            coltot = sub.sum();
            break;
        default:
            throw Error("unknown operation");
    }
    return coltot;
};
export const part1 = (lines: string[]): number => {
    console.log(
        "Part 1: What is the grand total found by adding together all of the answers to the individual problems?",
    );
    const parsed: string[][] = [];
    lines.forEach((line) => {
        // p(line)
        // p(line.trim().replace(/\s+/g, " "));
        parsed.push(
            line.trim().replace(/\s+/g, " ").split(" "),
        );
    });
    // p(parsed);
    // perform the calc
    let grandTot = 0;
    for (let col = 0; col < parsed[0].length; col++) {
        p(col);
        let colTot = getColTot(parsed, col);
        p("coltot of colum", col, "=", colTot);
        grandTot += colTot;
    }

    return grandTot;
};
export const part2 = (lines: string[]): number => {
    console.log("Part 2: x");
    return 0;
};

function* d06(input: string): Generator<number> {
    console.log("Day 6: Trash Compactor");
    const lines = input.trim().split("\n");
    yield part1(lines);
    yield part2(lines);
}

export default d06;
