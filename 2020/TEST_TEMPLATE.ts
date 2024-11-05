import { assertEquals } from "jsr:@std/assert";

import { part1, part2 } from "./d_DAY_.ts";

const testinput = `
`.trim().split("\n").map((line) => Number(line));
Deno.test("part 1", () => {
  assertEquals(part1(testinput), -1);
});
// Deno.test("part 2", () => {
//   assertEquals(part2(testinput), -1);
// });
