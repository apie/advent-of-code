import { assertEquals } from "jsr:@std/assert/equals";
import memoize from "jsr:@korkje/memz";
import "./util.ts";

const getMiddlePageNumber = (pageNumbers: number[]) =>
    pageNumbers[Math.trunc(pageNumbers.length / 2)];

let rules: {
    [x: string]: number;
}[] = [];

const sorter = memoize((second: number, first: number) =>
    rules.filter((
            rule,
        ) => Object.values(rule).includes(first)
        ).find((rule) => rule[second] === first)
        ? -1
        : 1
);

const pageUpdateValid = (
    pageUpdate: number[],
): boolean => pageUpdate.join(",") === [...pageUpdate].sort(sorter).join(",");

export const part1 = (lines: string[]): number => {
    // Find correctly ordered
    // Sum up the middle updates
    const [rulesStr, pagesStr] = lines;
    rules = rulesStr.trim().split("\n").map((rule) => {
        const pageNr = rule.split("|").map((n) => Number(n));
        return { [pageNr[0]]: pageNr[1] };
    });

    if (pagesStr.startsWith("75,47,61,53,29")) {
        const pageUpdates = pagesStr.split("\n").map((pageUpdateStr) =>
            pageUpdateStr.split(",").map((page) => Number(page))
        );
        assertEquals(pageUpdateValid(pageUpdates[0]), true, "0");
        assertEquals(pageUpdateValid(pageUpdates[1]), true, "1");
        assertEquals(pageUpdateValid(pageUpdates[2]), true, "2");
        assertEquals(pageUpdateValid(pageUpdates[3]), false, "3");
        assertEquals(pageUpdateValid(pageUpdates[4]), false, "4");
        assertEquals(pageUpdateValid(pageUpdates[5]), false, "5");
    }

    return pagesStr.split("\n").map((pageUpdateStr) =>
        pageUpdateStr.split(",").map((page) => Number(page))
    ).filter((pageUpdate) => pageUpdateValid(pageUpdate)).map((
        pageUpdate,
    ) => getMiddlePageNumber(pageUpdate)).sum();
};
export const part2 = (lines: string[]): number => {
    // Find incorrectly ordered
    // Order them
    // Sum up the middle updates
    const [_rulesStr, pagesStr] = lines;
    return pagesStr.split("\n").map((pageUpdateStr) =>
        pageUpdateStr.split(",").map((page) => Number(page))
    ).filter((pageUpdate) => !pageUpdateValid(pageUpdate)).map((
        pageUpdate,
    ) => getMiddlePageNumber(pageUpdate.sort(sorter))).sum();
};

function d05(input: string): number[] {
    const lines = input.trim().split("\n\n");
    return [
        part1(lines),
        part2(lines),
    ];
}

export default d05;
