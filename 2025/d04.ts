import "./util.ts";
import { Grid, p, Point } from "./util.ts";

export const part1 = (lines: string[]): number => {
    console.log(
        "Part 1: How many rolls of paper can be accessed by a forklift?",
    );
    const g = new Grid(lines);
    const pointArray: Point[] = [];
    let tot = 0;
    g.walkGrid((x, y) => {
        // Only check the places where a roll of paper lies
        const gp = new Point(x, y);
        if (g.isFree(gp)) return;
        // p(gp)
        // p(gp.getAdjacent());
        const blockedAj = gp.getAdjacent().filter((aj) => g.onGrid(aj)).map((
            aj,
        ) => g.isBlocked(aj)).count(true);
        // p(gp, blockedAj );
        if (blockedAj < 4) {
            pointArray.push(gp);
            tot++;
        }
    });
    g._dbg_printv(pointArray, "x");
    return tot;
};
export const part2 = (lines: string[]): number => {
    return 0;
};

function* d04(input: string): Generator<number> {
    console.log("Day 4: Printing Department");
    const lines = input.trim().split("\n");
    yield part1(lines);
    yield part2(lines);
}

export default d04;
