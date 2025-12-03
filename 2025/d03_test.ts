import { assertEquals } from "jsr:@std/assert@1.0.11";

import { part1, part2 } from "./d03.ts";

const testinput = `
987654321111111
811111111111119
234234234234278
818181911112111
`.trim().split("\n");
Deno.test("part 1", () => {
  assertEquals(part1(testinput), 357);
});
// Deno.test("part 2", () => {
//   assertEquals(part2(testinput), -1);
// });
