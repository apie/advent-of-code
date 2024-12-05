import { assertEquals } from "jsr:@std/assert";

import { part1, part2 } from "./d04.ts";

const testinput = `
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
`.trim().split("\n");
Deno.test("part 1", () => {
  assertEquals(part1(testinput), 18);
});
// Deno.test("part 2", () => {
//   assertEquals(part2(testinput), -1);
// });
