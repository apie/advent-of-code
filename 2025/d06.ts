import { assert } from "jsr:@std/assert@1.0.11/assert";
import "./util.ts";
import { Grid, p } from "./util.ts";

const getColSubTot = (colArr: string[]): number => {
    p("~~~~~~~~~get subtot:");
    //calculate subtot of latest col
    const op = colArr.shift();
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
    const sub: string[] = [];
    sub.push(parsed[parsed.length - 1][col]); //operation is first item
    for (let row = 0; row < parsed.length - 1; row++) {
        sub.push(parsed[row][col]);
    }
    return getColSubTot(sub);
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
    const g = new Grid(lines);
    g._dbg_printv();
    let vals = "";
    let colArr: string[] = [];
    let tot = 0;
    g.walkGridRowFirst((x, _y, val: string) => {
        val = val?.trim();
        // p(x,_y,val);
        if (val?.match(/\d/)) { // digits can be concatenated to val
            vals += val;
        } else if (val) { // operation can be added to the array
            colArr.push(val);
        }

        if (x === lines.length - 1) {
            // p('last row')
            if (vals === "") {
                const subtot = getColSubTot(colArr);
                p("subtot:", subtot);
                tot += subtot;
                colArr = [];
            } else {
                p("vals:", vals);
                colArr.push(vals);
                vals = ""; //reset after reaching last row
            }
        }
    });
    // Rightmost col:
    const subtot = getColSubTot(colArr);
    p("subtot:", subtot);
    tot += subtot;
    colArr = [];
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
