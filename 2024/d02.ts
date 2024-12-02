import "./util.ts";

type Treport = number[];

const parseReport = (unparsedReport: string): Treport =>
    unparsedReport.split(" ").map((char) => Number(char));

const isReportSafe = (report: Treport): boolean => {
    console.log(report);
    let totsign = 0;
    const a = report.reduce((prev, val) => {
        const diff = prev - val;
        const sign = diff / Math.abs(diff);
        console.log(prev, val, "sign", sign);
        totsign += sign;
        return [1, 2, 3].includes(Math.abs(diff)) ? val : NaN;
    });
    console.debug("totsign", totsign, a);
    if (Number.isNaN(a)) return false;
    if (Math.abs(totsign) !== report.length - 1) return false;
    return true;
};
export const part1 = (lines: string[]): number => {
    // Check which reports are safe:
    // Either all increasing or all decreasing
    // Any two adjacent levels differ by at least one and at most three .
    console.log(lines);
    // const unparsedReport = lines[0];
    // console.log(unparsedReport);
    // const report = parseReport(unparsedReport);
    // console.log(report);
    // console.log(isReportSafe(report));
    // return 0;
    const ans = lines.map((line) => parseReport(line)).map((report) =>
        isReportSafe(report)
    ).count(true);
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
