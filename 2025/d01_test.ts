import { assertEquals } from "jsr:@std/assert";

import { part1, part2 } from "./d01.ts";

const testinput = `
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
`.trim().split("\n");
Deno.test("part 1", () => {
  assertEquals(part1(testinput), 3);
});
Deno.test("part 2", () => {
  assertEquals(part2(testinput), 6);
});
const testinput2 = `
R1000
`.trim().split("\n");
Deno.test("part 2.2", () => {
  assertEquals(part2(testinput2), 10);
});
