import { assert } from "jsr:@std/assert/assert";
import "./util.ts";

export const getseatID = (boardingPass: string): number => {
    console.log("*" + boardingPass + "*");
    const boardingPassA = boardingPass.split("");
    let row = [0, 127];
    // console.log(row);
    while (boardingPassA.length > 3) {
        const char = boardingPassA.shift();
        // console.log(char);
        switch (char) {
            case "F":
                row[1] = row[1] - (1 + row[1] - row[0]) / 2;
                break;
            case "B":
                row[0] = row[0] + (1 + row[1] - row[0]) / 2;
                break;
            default:
                throw Error("Unknown character " + char);
        }
        // console.log(row);
    }
    assert(row[0] === row[1], "Didnt find row");
    let col = [0, 7];
    // console.log(col);
    while (boardingPassA.length) {
        const char = boardingPassA.shift();
        // console.log(char);
        switch (char) {
            case "L":
                col[1] = col[1] - (1 + col[1] - col[0]) / 2;
                break;
            case "R":
                col[0] = col[0] + (1 + col[1] - col[0]) / 2;
                break;
            default:
                throw Error("Unknown character " + char);
        }
        // console.log(col);
    }
    assert(col[0] === col[1], "Didnt find col");

    return row[0] * 8 + col[0];
};
export const part1 = (lines: string[]): number => {
    return lines.map((line) => getseatID(line)).max();
};
export const part2 = (lines: string[]): number => {
    return 0;
};

function d05(input: string): number[] {
    const lines = input.trim().split("\n").filter((line) => line.match(/\w/));
    return [
        part1(lines),
        part2(lines),
    ];
}

export default d05;
