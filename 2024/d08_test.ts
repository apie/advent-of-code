import { assertEquals } from "jsr:@std/assert";

import { part1, part2 } from "./d08.ts";

const testinput = `
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
`.trim().split("\n");
const testinput2 = `
..........
..........
..........
....a.....
........a.
.....a....
..........
..........
..........
..........
`.trim().split("\n");
Deno.test("part 1", () => {
  assertEquals(part1(testinput2), 4);
});
Deno.test("part 1", () => {
  assertEquals(part1(testinput), 14);
});
const testinput3 = `
T.........
...T......
.T........
..........
..........
..........
..........
..........
..........
..........
`.trim().split("\n");

Deno.test("part 2a", () => {
  assertEquals(part2(testinput3), 9);
});
Deno.test("part 2", () => {
  assertEquals(part2(testinput), 34);
});
