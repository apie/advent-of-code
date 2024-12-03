import "./util.ts";

export const part1 = (lines: string[]): number => {
    // Find only real mul instructions: mul(123,123)
    // Execute them and sum the results
    return lines.map((line) => {
        const m = line.match(/mul\(\d{1,3},\d{1,3}\)/g);
        if (!m) return 0;
        const multiplied = m.map((expr) => {
            const j = expr.match(/(\d+),(\d+)/);
            console.log(expr);
            if (!j) return 0;
            // console.log(j[2])
            return Number(j[1]) * Number(j[2]);
        });
        console.log(multiplied);
        console.log(multiplied.sum());
        return multiplied.sum();
    }).sum();
};
export const part2 = (lines: string[]): number => {
    return 0;
};

function d03(input: string): number[] {
    const lines = input.trim().split("\n");
    return [
        part1(lines),
        part2(lines),
    ];
}

export default d03;
