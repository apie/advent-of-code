import { assertEquals } from "jsr:@std/assert";

import { part1, part2 } from "./d02.ts";

const testinput = `
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
`.trim().split("\n");
Deno.test("part 1", () => {
  assertEquals(part1(testinput), 2);
});
Deno.test("part 2", () => {
  assertEquals(part2(testinput), 4);
});
