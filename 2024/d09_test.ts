import { assertEquals } from "jsr:@std/assert";

import { part1, part2 } from "./d09.ts";

const testinput = `
2333133121414131402
`.trim().split("\n");
const testinput2 = `
12345
`.trim().split("\n");
Deno.test("part 1a", () => {
  assertEquals(part1(testinput2), 60);
});
Deno.test("part 1", () => {
  assertEquals(part1(testinput), 1928);
});
// Deno.test("part 2", () => {
//   assertEquals(part2(testinput), -1);
// });
