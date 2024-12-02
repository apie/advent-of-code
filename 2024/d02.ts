import "./util.ts";

type Treport = number[];

const parseReport = (unparsedReport: string): Treport =>
    unparsedReport.split(" ").map((char) => Number(char));

const isReportSafe = (report: Treport): boolean => {
    //TODO
    return false;
};
export const part1 = (lines: string[]): number => {
    // Check which reports are safe:
    // Either all increasing or all decreasing
    // Any two adjacent levels differ by at least one and at most three .
    console.log(lines);
    const unparsedReport = lines[0];
    console.log(unparsedReport);
    const report = parseReport(unparsedReport);
    console.log(report);
    console.log(isReportSafe(report));
    const ans = lines.map((line) => parseReport(line)).map((report) =>
        isReportSafe(report)
    )
        .count(true);
    console.log(ans);
    return ans;
};
export const part2 = (lines: string[]): number => {
    return 0;
};

function d02(input: string): number[] {
    const lines = input.trim().split("\n");
    return [
        part1(lines),
        part2(lines),
    ];
}

export default d02;
