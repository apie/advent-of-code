import { assertEquals } from "jsr:@std/assert";

import { part1, part2 } from "./d02.ts";

  const testinput = "1-3 a: abcde\n\
1-3 b: cdefg\n\
2-9 c: ccccccccc";
Deno.test("part 1", () => {
  assertEquals(part1(testinput), 2);
});
Deno.test("part 2", () => {
  assertEquals(part2(testinput), 1);
});
