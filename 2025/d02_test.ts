import { assertEquals } from "jsr:@std/assert@1.0.11";

import { part1, part2 } from "./d02.ts";

const testinput = `
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
`.trim().split("\n");
Deno.test("part 1", () => {
  assertEquals(part1(testinput), 1227775554);
});
// Deno.test("part 2", () => {
//   assertEquals(part2(testinput), -1);
// });
