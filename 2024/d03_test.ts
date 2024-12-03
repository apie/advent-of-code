import { assertEquals } from "jsr:@std/assert";

import { part1, part2 } from "./d03.ts";

const testinput = `
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
`.trim().split("\n");
Deno.test("part 1", () => {
  assertEquals(part1(testinput), 161);
});
const testinput2 = `
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
`.trim().split("\n");
Deno.test("part 2", () => {
  assertEquals(part2(testinput2), 48);
});
