import { assert } from "jsr:@std/assert/assert";
import "./util.ts";

export const getseatID = (boardingPass: string): number => {
    // console.log("*" + boardingPass + "*");
    const boardingPassArr = boardingPass.split("");
    const row = [0, 127];
    while (boardingPassArr.length > 3) {
        const char = boardingPassArr.shift();
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
    }
    assert(row[0] === row[1], "Didnt find row");
    const col = [0, 7];
    while (boardingPassArr.length) {
        const char = boardingPassArr.shift();
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
    }
    assert(col[0] === col[1], "Didnt find col");
    return row[0] * 8 + col[0];
};

export const part1 = (lines: string[]): number =>
    lines.map((line) => getseatID(line)).max();

const findMissingSeatID = (lines: string[]): number => {
    const mySeatArr = lines.map((line) => {
        return getseatID(line);
    }).filter((sId, _i, arr) =>
        // Filter out three in a row
        !(
            arr.includes(sId) && arr.includes(sId - 1) && arr.includes(sId + 1)
        )
        // Find candidate upper neighbour
    ).filter((sId, _id, arr) => arr.includes(sId - 2));
    assert(mySeatArr.length === 1, "Found multiple seats");
    const mySeat = mySeatArr[0] - 1;
    return mySeat;
};

export const part2 = (lines: string[]): number => findMissingSeatID(lines);

function d05(input: string): number[] {
    const lines = input.trim().split("\n").filter((line) => line.match(/\w/));
    return [
        part1(lines),
        part2(lines),
    ];
}

export default d05;
