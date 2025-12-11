import "./util.ts";
import { Grid, p, Point } from "./util.ts";

const getAccessibleRolls = (g: Grid): Point[] =>
    Array.from(g.walkGrid())
        .filter(([pt, _val]) =>
            // Only check the places where a roll of paper lies
            !g.isFree(pt)
        )
        .filter(([pt, _val]) =>
            // Filter number of adjacent, on grid, blocked rolls, that is less than 4
            pt.getAdjacent().filter((aj) => g.onGrid(aj))
                .map((
                    aj,
                ) => g.isBlocked(aj)).count(true) < 4
        ).map(([pt, _val]) => pt);

export const part1 = (lines: string[]): number => {
    console.log(
        "Part 1: How many rolls of paper can be accessed by a forklift?",
    );
    const g = new Grid(lines);
    const accessibleRolls = getAccessibleRolls(g);
    g._dbg_printv(accessibleRolls, "x");
    return accessibleRolls.length;
};
const removeRolls = (g: Grid, rolls: Point[]) => {
    rolls.forEach((roll) => g.replaceCharAt(roll, "."));
};
export const part2 = (lines: string[]): number => {
    console.log(
        "Part 2: How many rolls of paper in total can be removed by the Elves and their forklifts?",
    );
    const g = new Grid(lines);
    let totalRemoved = 0;
    let accessibleRolls;
    do {
        accessibleRolls = getAccessibleRolls(g);
        p("Going to remove", accessibleRolls.length, "rolls:");
        g._dbg_printv(accessibleRolls, "@");
        removeRolls(g, accessibleRolls);
        totalRemoved += accessibleRolls.length;
    } while (accessibleRolls.length);
    return totalRemoved;
};

function* d04(input: string): Generator<number> {
    console.log("Day 4: Printing Department");
    const lines = input.trim().split("\n");
    yield part1(lines);
    yield part2(lines);
}

export default d04;
