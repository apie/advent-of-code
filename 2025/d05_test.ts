import { assertEquals } from "jsr:@std/assert@1.0.11";

import { part1, part2 } from "./d05.ts";

const testinput = `
3-5
10-14
16-20
12-18

1
5
8
11
17
32
`.trim().split("\n");
Deno.test("part 1", () => {
  assertEquals(part1(testinput), 3);
});
// Deno.test("part 2", () => {
//   assertEquals(part2(testinput), -1);
// });
