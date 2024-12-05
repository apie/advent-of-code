import { assertEquals } from "jsr:@std/assert/equals";
import "./util.ts";

const getMiddlePageNumber = (pageNumbers: number[]) =>
    pageNumbers[Math.trunc(pageNumbers.length / 2)];

const pageUpdateValid = (
    rules: { [x: number]: number }[],
    pageUpdate: number[],
): boolean => {
    //FIXME
    const s = [...pageUpdate].sort((a, b) => {
        const arule = rules.find((rule) => rule[a] !== undefined);
        if (!arule) return 0;
        return arule[a] === b ? -1 : 1;
    });
    console.log("n", pageUpdate);
    console.log("s", s);
    return pageUpdate.join(",") === s.join(",");
};
export const part1 = (lines: string[]): number => {
    const [rulesStr, pagesStr] = lines;
    // console.log(rulesStr);
    const rules = rulesStr.trim().split("\n").map((rule) => {
        const pageNr = rule.split("|").map((n) => Number(n));
        return { [pageNr[0]]: pageNr[1] };
    });
    console.log(rules);

    const pageUpdates = pagesStr.split("\n").map((pageUpdateStr) =>
        pageUpdateStr.split(",").map((page) => Number(page))
    );
    assertEquals(pageUpdateValid(rules, pageUpdates[0]), true, "0");
    assertEquals(pageUpdateValid(rules, pageUpdates[1]), true, "1");
    assertEquals(pageUpdateValid(rules, pageUpdates[2]), true, "2");
    assertEquals(pageUpdateValid(rules, pageUpdates[3]), false, "3");
    assertEquals(pageUpdateValid(rules, pageUpdates[4]), false, "4");
    assertEquals(pageUpdateValid(rules, pageUpdates[5]), false, "5");
    // return -1; // FIXME

    return pagesStr.split("\n").map((pageUpdateStr) =>
        pageUpdateStr.split(",").map((page) => Number(page))
    ).filter((pageUpdate) => pageUpdateValid(rules, pageUpdate)).map((
        pageUpdate,
    ) => getMiddlePageNumber(pageUpdate)).sum();
};
export const part2 = (lines: string[]): number => {
    return 0;
};

function d05(input: string): number[] {
    const lines = input.trim().split("\n\n");
    return [
        part1(lines),
        part2(lines),
    ];
}

export default d05;
