import "./util.ts";
import { p } from "./util.ts";

const isFresh = (ingredient: number, freshRanges: number[][]): boolean => {
    return !!freshRanges.find((range) => {
        const [from, to] = range;
        return ingredient.between(from, to);
    });
};
export const part1 = (lines: string[]): number => {
    // p(lines)
    const freshIngredientRanges: number[][] = [];
    let line = "\o/";
    while (line != "") {
        line = lines.shift() || "";
        // p(line)
        if (line) {
            const from_to = line.split("-").map((s) => Number(s));
            freshIngredientRanges.push(from_to);
        }
    }
    p("freshranges", freshIngredientRanges);
    p("ingredients", lines);
    //rest of lines contain the ingredients
    return lines.map((line) => isFresh(Number(line), freshIngredientRanges))
        .count(
            true,
        );
};
export const part2 = (lines: string[]): number => {
    return 0;
};

function* d05(input: string): Generator<number> {
    const lines = input.trim().split("\n");
    yield part1(lines);
    yield part2(lines);
}

export default d05;
