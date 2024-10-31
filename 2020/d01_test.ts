import { assertEquals } from "jsr:@std/assert";

import { part1, part2 } from "./d01.ts";

const testinput = `1721
979
366
299
675
1456`.trim().split("\n").map((line) => Number(line));
Deno.test("part 1", () => {
  assertEquals(part1(testinput), 514579);
});
// Deno.test("part 2", () => {
//   assertEquals(part2(testinput), -1);
// });
