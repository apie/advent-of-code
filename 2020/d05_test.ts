import { assertEquals } from "jsr:@std/assert";

import { getseatID, part1 } from "./d05.ts";

Deno.test("part 1 getseatID 1", () => {
  const testinput = `
FBFBBFFRLR
`.trim();
  assertEquals(getseatID(testinput), 357);
});
Deno.test("part 1 getseatID 2", () => {
  const testinput = `
BFFFBBFRRR
`.trim();
  assertEquals(getseatID(testinput), 567);
});
Deno.test("part 1 getseatID 3", () => {
  const testinput = `
FFFBBBFRRR
`.trim();
  assertEquals(getseatID(testinput), 119);
});
Deno.test("part 1 getseatID 4", () => {
  const testinput = `
BBFFBBFRLL
`.trim();
  assertEquals(getseatID(testinput), 820);
});
const testinput = `
FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL
`.trim().split("\n");
Deno.test("part 1", () => {
  assertEquals(part1(testinput), 820);
});
