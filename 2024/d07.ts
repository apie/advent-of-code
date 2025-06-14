import { permutationsWithReplacement } from "https://deno.land/x/combinatorics/mod.ts";
import "./util.ts";
import { p } from "./util.ts";

export const add = (a: number, b: number): number => a + b;
export const mul = (a: number, b: number): number => a * b;
export const con = (a: number, b: number): number =>
    Number(String(a) + String(b));
export const getTotalCalibration = (
    lines: string[],
    OPERATORS: CallableFunction[],
): number => {
    let totalCalibrationResult = 0;
    lines.forEach((line) => {
        const testValue = Number(line.split(":")[0]);
        p();
        p(line);
        const numbers = line.split(":")[1].trim().split(" ").map((nstring) =>
            Number(nstring)
        );
        // p(numbers);
        const opPermutations = permutationsWithReplacement(
            OPERATORS,
            numbers.length - 1,
        );
        let foundLine = false;
        // loop all possible combinations of the operators until we have a match
        opPermutations.forEach((opPermutation) => {
            if (foundLine) return;
            p(opPermutation);

            const res = numbers.slice(1).reduce((prev, num, i) => {
                const op = opPermutation[i];
                p(
                    "prev",
                    prev,
                    "operator",
                    op.name,
                    "num",
                    num,
                );
                return op(prev, num);
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
    p(lines);
    return totalCalibrationResult;
};
export const part1 = (lines: string[]): number =>
    getTotalCalibration(lines, [add, mul]);

export const part2 = (lines: string[]): number =>
    getTotalCalibration(lines, [add, mul, con]);

function d07(input: string): number[] {
    const lines = input.trim().split("\n");
    return [
        part1(lines),
        part2(lines),
    ];
}

export default d07;
