export const part1 = (lines: number[]): number => {
    return 0;
};
export const part2 = (lines: number[]): number => {
    return 0;
};

function d_DAY_(input: string): number[] {
    const lines = input.trim().split("\n").filter((line) => line.match(/^\d/))
        .map((line) => Number(line));
    return [
        part1(lines),
        part2(lines),
    ];
}

export default d_DAY_;
