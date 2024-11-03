import { assertEquals } from "jsr:@std/assert";

import { part1, part2 } from "./d03.ts";

const testinput = `
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
`.trim().split("\n")
Deno.test("part 1", () => {
  assertEquals(part1(testinput), 7);
});
Deno.test("part 2", () => {
  assertEquals(part2(testinput), 336);
});
