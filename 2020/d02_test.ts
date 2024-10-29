import { assertEquals } from "jsr:@std/assert";

import { part1 } from "./d02.ts";

Deno.test("part 1", () => {
  const testinput = "1-3 a: abcde\n\
1-3 b: cdefg\n\
2-9 c: ccccccccc";
  assertEquals(part1(testinput), 2);
});
