import "./util.ts";
import { Grid, p, Point } from "./util.ts";

const getAccessibleRolls = (g: Grid): Point[] => {
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
    return pointArray;
};
export const part1 = (lines: string[]): number => {
    console.log(
        "Part 1: How many rolls of paper can be accessed by a forklift?",
    );
    const g = new Grid(lines);
    const pointArray = getAccessibleRolls(g);
    g._dbg_printv(pointArray, "x");
    return pointArray.length;
};
const removeRolls = (g: Grid, rolls: Point[]) => {
    rolls.forEach((roll) => {
        g.g[roll.x] = g.g[roll.x].replaceCharAt(roll.y, ".");
    });
};
export const part2 = (lines: string[]): number => {
    console.log(
        "Part 2: How many rolls of paper in total can be removed by the Elves and their forklifts?",
    );
    let g = new Grid(lines);
    let totalRemoved = 0;
    let accessibleRolls = [new Point(12345, 6789)]; // initialize with dummy
    while (accessibleRolls.length) {
        accessibleRolls = getAccessibleRolls(g);
        p("Going to remove", accessibleRolls.length, "rolls:");
        g._dbg_printv(accessibleRolls, "@");
        totalRemoved += accessibleRolls.length;
        removeRolls(g, accessibleRolls);
    }
    g._dbg_printv();
    return totalRemoved;
};

function* d04(input: string): Generator<number> {
    console.log("Day 4: Printing Department");
    const lines = input.trim().split("\n");
    yield part1(lines);
    yield part2(lines);
}

export default d04;
