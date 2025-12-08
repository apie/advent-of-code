import { assertEquals } from "jsr:@std/assert@1.0.11";

import { part1, part2 } from "./d06.ts";

const testinput = `
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + 
`.trim().split("\n");
Deno.test("part 1", () => {
  assertEquals(part1(testinput), 4277556);
});
Deno.test("part 2", () => {
  assertEquals(part2(testinput), 3263827);
});
