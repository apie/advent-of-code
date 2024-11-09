import { assertEquals } from "jsr:@std/assert";

import { part1, part2 } from "./d06.ts";

const testinput = `
abc

a
b
c

ab
ac

a
a
a
a

b
`.trim().split("\n\n");
Deno.test("part 1", () => {
  assertEquals(part1(testinput), 11);
});
// Deno.test("part 2", () => {
//   assertEquals(part2(testinput), -1);
// });
