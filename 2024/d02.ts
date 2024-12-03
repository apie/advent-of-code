import "./util.ts";

type Treport = number[];

const parseReport = (unparsedReport: string): Treport =>
    unparsedReport.split(" ").map((char) => Number(char));

const isReportSafe = (report: Treport): boolean => {
    let totsign = 0;
    const a = report.reduce((prev, val) => {
        const diff = prev - val;
        const sign = diff / Math.abs(diff);
        totsign += sign;
        return [1, 2, 3].includes(Math.abs(diff)) ? val : NaN;
    });
    if (Number.isNaN(a)) return false;
    if (Math.abs(totsign) !== report.length - 1) return false;
    return true;
};
export const part1 = (lines: string[]): number => {
    // Check which reports are safe:
    // Either all increasing or all decreasing
    // Any two adjacent levels differ by at least one and at most three .
    return lines.map((line) => parseReport(line)).map((report) =>
        isReportSafe(report)
    ).count(true);
};
const isReportSafeWhenRemovingASingleLevel = (report: Treport): boolean =>
    report.reduce(
        (found, _level, i) =>
            found || isReportSafe(report.filter((_level, j) => j !== i)),
        false,
    );

export const part2 = (lines: string[]): number => {
    // Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.
    return lines.map((line) => parseReport(line)).map((report) =>
        isReportSafe(report) || isReportSafeWhenRemovingASingleLevel(report)
    ).count(true);
};

function d02(input: string): number[] {
    const lines = input.trim().split("\n");
    // console.log(lines);
    return [
        part1(lines),
        part2(lines),
    ];
}

export default d02;
