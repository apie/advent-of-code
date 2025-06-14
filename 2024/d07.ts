import "./util.ts";
import { p } from "./util.ts";

import { array } from "jsr:@korkje/ncp";
const car = array;

export const add = (a: number, b: number): number => a + b;
export const mul = (a: number, b: number): number => a * b;
const OPERATORS = [
    add,
    mul,
];
export const part1 = (lines: string[]): number => {
    let totalCalibrationResult = 0;
    lines.forEach((line, nline) => {
        const testValue = Number(line.split(":")[0]);
        p();
        p(line);
        const numbers = line.split(":")[1].trim().split(" ").map((nstring) =>
            Number(nstring)
        );
        // p(numbers);
        const oparray = OPERATORS.map((_op, i) => i);
        const narray = numbers.slice(1).map((_n, i) => i % OPERATORS.length);
        p("oparray", oparray);
        p("narray", narray);
        let opPermutations: number[][] = [[]];
        switch (numbers.length - 1) {
            case 1:
                opPermutations = oparray.map((op) => [op]);
                break;
            case 2:
                opPermutations = car(narray, oparray);
                break;
            case 3:
                opPermutations = car(narray, oparray, oparray);
                break;
            case 4:
                opPermutations = car(narray, oparray, oparray, oparray);
                break;
            case 5:
                opPermutations = car(
                    narray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                );
                break;
            case 6:
                opPermutations = car(
                    narray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                );
                break;
            case 7:
                opPermutations = car(
                    narray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                );
                break;
            case 8:
                opPermutations = car(
                    narray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                );
                break;
            case 9:
                opPermutations = car(
                    narray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                );
                break;
            case 10:
                opPermutations = car(
                    narray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                );
                break;
            case 11:
                opPermutations = car(
                    narray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                    oparray,
                );
                break;
            default:
                throw Error(`not implemented ${numbers.length - 1}`);
        }
        p("opPermutations", opPermutations);
        let foundLine = false;
        // loop all possible combinations of the operators until we have a match
        opPermutations.forEach((opPermutation) => {
            if (foundLine) return;
            p(opPermutation);

            const res = numbers.slice(1).reduce((prev, num, i) => {
                const opnum = opPermutation[i];
                const op = OPERATORS[opnum];
                p(
                    "prev",
                    prev,
                    "operator",
                    op.name,
                    "num",
                    num,
                );
                return op(num, prev);
            }, numbers[0] || 0);
            if (res === testValue) {
                totalCalibrationResult += testValue;
                p("found!");
                foundLine = true;
                return;
            }
            p("res:", res);
        });
    });
    return totalCalibrationResult;
};
export const part2 = (lines: string[]): number => {
    return 0;
};

function d07(input: string): number[] {
    const lines = input.trim().split("\n");
    return [
        part1(lines),
        part2(lines),
    ];
}

export default d07;
