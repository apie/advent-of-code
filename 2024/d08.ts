import "./util.ts";
import { Grid, p, Point, sortPoints } from "./util.ts";
import { combinations } from "https://deno.land/x/combinatorics/mod.ts";

class Antenna extends Point {
    id: string;
    constructor(x: number, y: number, id: string) {
        super(x, y);
        this.id = id;
    }
}
const getAntinodes = (a: Antenna, b: Antenna): Point[] => {
    // get distance between
    p("getting distance...", a, b);
    const distance = {
        x: a.x - b.x,
        y: a.y - b.y,
    };
    p("distance =", distance);
    // add distance on both sides to get the antinodes
    return [
        new Point(a.x + 1 * (distance.x), a.y + 1 * (distance.y)),
        new Point(b.x + -1 * (distance.x), b.y + -1 * (distance.y)),
    ];
};
const getAntinodes2 = (a: Antenna, b: Antenna): Point[] => {
    // get distance between
    p("getting distance...", a, b);
    const distance = {
        x: a.x - b.x,
        y: a.y - b.y,
    };
    p("distance =", distance);
    // add distance on both sides to get the antinodes
    const antinodes: Point[] = [];
    let dimension = 0;
    while (dimension <= 100) {
        antinodes.push(
            new Point(
                a.x + dimension * (distance.x),
                a.y + dimension * (distance.y),
            ),
        );
        antinodes.push(
            new Point(
                a.x + -dimension * (distance.x),
                a.y + -dimension * (distance.y),
            ),
        );
        dimension += 1;
    }
    return antinodes;
};
const withinBounds = (bounds: number[], antinode: Point): boolean => {
    return antinode.x.between(0, bounds[0]) && antinode.y.between(0, bounds[1]);
};
export const getUniqueAntinodesOnMap = (
    lines: string[],
    antinodesFunction: (a: Antenna, b: Antenna) => Point[],
): number => {
    const antennas: Antenna[] = [];
    const bounds = [lines[0].length - 1, lines.length - 1];
    lines.forEach((line, lineno) => {
        line.split("").forEach((col, colno) => {
            if (col !== ".") {
                antennas.push(new Antenna(colno, lineno, col));
            }
        });
    });
    p(antennas);
    const ids = new Set(antennas.map((a) => a.id));
    p(ids);
    const g = new Grid(lines);
    const allAntinodes = new Map<string, Point>(); // use Map and not Set since we have objects
    ids.forEach((id) => {
        const antennapairs = Array.from(
            combinations(antennas.filter((a) => a.id === id), 2),
        );
        antennapairs.forEach((pair) => {
            // p("pair", pair);
            const [a, b] = pair;
            const antinodes = antinodesFunction(a, b);
            p("antinodes", antinodes);
            antinodes.forEach((antinode) => {
                if (withinBounds(bounds, antinode)) {
                    allAntinodes.set(antinode.getUniqueKey(), antinode);
                }
            });

            g._dbg_printv(
                [
                    new Point(a.x, a.y), // must convert Antenna to Point to pass to this dbg func
                    new Point(b.x, b.y), // must convert Antenna to Point to pass to this dbg func
                    ...Array.from(antinodes),
                ],
                "",
                true,
            );
        });
    });
    p(allAntinodes);
    sortPoints(Array.from(allAntinodes.values())).forEach((an) => p(an));
    g._dbg_printv(
        [
            ...Array.from(allAntinodes.values()),
        ],
        "",
        true,
    );
    return allAntinodes.size;
};

export const part1 = (lines: string[]): number =>
    getUniqueAntinodesOnMap(lines, getAntinodes);
export const part2 = (lines: string[]): number =>
    getUniqueAntinodesOnMap(lines, getAntinodes2);
function d08(input: string): number[] {
    const lines = input.trim().split("\n");
    return [
        part1(lines),
        part2(lines),
    ];
}

export default d08;
