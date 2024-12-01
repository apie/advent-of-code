import { assertEquals } from "jsr:@std/assert";

import { part1, part2 } from "./d01.ts";

const testinput = `
3   4
4   3
2   5
1   3
3   9
3   3
`.trim().split("\n");
Deno.test("part 1", () => {
  assertEquals(part1(testinput), 11);
});
// Deno.test("part 2", () => {
//   assertEquals(part2(testinput), -1);
// });
