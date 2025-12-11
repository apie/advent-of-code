import { assert } from "jsr:@std/assert@1.0.11/assert";
import "./util.ts";
import { Grid, p } from "./util.ts";

const getColSubTot = (op: string, colArr: string[]): number => {
    p("~~~~~~~~~get subtot:");
    switch (op) {
        case "*":
            return colArr.prod(); //items converted to number automatically
        case "+":
            return colArr.sum(); //items converted to number automatically
        default:
            throw Error("unknown operation " + op);
    }
};
const getColTot = (parsed: string[][], col: number): number => {
    const op = parsed[parsed.length - 1][col];
    const sub = parsed.slice(0, parsed.length - 1).map((row) => row[col]);
    return getColSubTot(op, sub);
};
export const part1 = (lines: string[]): number => {
    console.log(
        "Part 1: What is the grand total found by adding together all of the answers to the individual problems?",
    );
    const parsed: string[][] = lines.map((line) =>
        line.trim().replace(/\s+/g, " ").split(" ")
    );
    // p(parsed);
    // perform the calc
    let grandTot = 0;
    for (let col = 0; col < parsed[0].length; col++) {
        const colTot = getColTot(parsed, col);
        p("coltot of colum", col, "=", colTot);
        grandTot += colTot;
    }
    return grandTot;
};
export const part2 = (lines: string[]): number => {
    console.log(
        "Part 2: What is the grand total found by adding together all of the answers to the individual problems?",
    );
    const g = new Grid(lines.map((line) => line += " ")); // add empty col on the right
    g._dbg_printv();
    let vals = "";
    let colArr: string[] = [];
    let tot = 0;
    let op = "";
    g.walkGridRowFirst().forEach(([pt, val]) => {
        val = val?.trim();
        if (val?.match(/\d/)) { // digits can be concatenated to val
            vals += val;
        } else if (val) { // operation
            op = val;
        }

        if (pt.x === lines.length - 1) {
            // last row
            if (vals === "") {
                const subtot = getColSubTot(op, colArr);
                p("subtot:", subtot);
                tot += subtot;
                colArr = [];
            } else {
                p("vals:", vals);
                colArr.push(vals);
            }
            vals = ""; // reset after reaching last row
        }
    });
    assert(colArr.length === 0, "colArr not empty");
    return tot;
};

function* d06(input: string): Generator<number> {
    console.log("Day 6: Trash Compactor");
    const lines = input.trim().split("\n");
    yield part1(lines);
    yield part2(lines);
}

export default d06;
