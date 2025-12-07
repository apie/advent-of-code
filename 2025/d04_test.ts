import { assertEquals } from "jsr:@std/assert@1.0.11";

import { part1, part2 } from "./d04.ts";

const testinput = `
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
`.trim().split("\n");
Deno.test("part 1", () => {
  assertEquals(part1(testinput), 13);
});
// Deno.test("part 2", () => {
//   assertEquals(part2(testinput), -1);
// });
