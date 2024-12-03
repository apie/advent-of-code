import "./util.ts";

export const part1 = (lines: string[]): number =>
    // Find only real mul instructions: mul(123,123)
    // Execute them and sum the results
    lines.map((line) =>
        line.match(/mul\(\d{1,3},\d{1,3}\)/g)?.map((expr) => {
            const operands = expr.match(/(\d+),(\d+)/);
            return operands && Number(operands[1]) * Number(operands[2]);
        }).sum()
    ).sum();

export const part2 = (lines: string[]): number => {
    let enabled = true;
    // Same as before but only in between do() and don't() instructions
    return lines.map((line) =>
        line.match(/do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)/g)?.map(
            (expr) => {
                if (expr.match(/do\(\)/)) enabled = true;
                else if (expr.match(/don't\(\)/)) enabled = false;
                const operands = expr.match(/(\d+),(\d+)/);
                return enabled && operands &&
                    Number(operands[1]) * Number(operands[2]);
            },
        ).sum()
    ).sum();
};

function d03(input: string): number[] {
    const lines = input.trim().split("\n");
    return [
        part1(lines),
        part2(lines),
    ];
}

export default d03;
