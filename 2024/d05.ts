import { assertEquals } from "jsr:@std/assert/equals";
import "./util.ts";

const getMiddlePageNumber = (pageNumbers: number[]) =>
    pageNumbers[Math.trunc(pageNumbers.length / 2)];

const pageUpdateValid = (
    rules: { [x: number]: number }[],
    pageUpdate: number[],
): boolean => {
    // console.log();
    const s = [...pageUpdate].sort((second, first) => {
        const arule = rules.filter((rule) =>
            (Object.values(rule).includes(second)) ||
            (Object.values(rule).includes(first)) ||
            (rule[first] !== undefined)
        );
        // console.debug("first", first, "second", second, "arule", arule);
        if (arule.length === 0) return 0;
        let retval = 1;
        arule.forEach((rule) => {
            // console.log(rule[second] === first);
            if (rule[second] === first) retval = -1;
        });
        return retval;
    });
    // console.log("n", pageUpdate);
    // console.log("s", s);
    // console.log(pageUpdate.join(",") === s.join(",") ? "EQUAL" : "NOT EQUAL");
    return pageUpdate.join(",") === s.join(",");
};
export const part1 = (lines: string[]): number => {
    const [rulesStr, pagesStr] = lines;
    // console.log(rulesStr);
    const rules = rulesStr.trim().split("\n").map((rule) => {
        const pageNr = rule.split("|").map((n) => Number(n));
        return { [pageNr[0]]: pageNr[1] };
    });
    // console.log(rules);

    const pageUpdates = pagesStr.split("\n").map((pageUpdateStr) =>
        pageUpdateStr.split(",").map((page) => Number(page))
    );
    if (pageUpdates[0].join(",") === "75,47,61,53,29") {
        assertEquals(pageUpdateValid(rules, pageUpdates[0]), true, "z0");
        assertEquals(pageUpdateValid(rules, pageUpdates[1]), true, "1");
        assertEquals(pageUpdateValid(rules, pageUpdates[2]), true, "2");
        assertEquals(pageUpdateValid(rules, pageUpdates[3]), false, "3");
        assertEquals(pageUpdateValid(rules, pageUpdates[4]), false, "4");
        assertEquals(pageUpdateValid(rules, pageUpdates[5]), false, "5");
        // return -1; // FIXME
    }

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
