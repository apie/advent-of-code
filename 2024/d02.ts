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
    const ans = lines.map((line) => parseReport(line)).map((report) =>
        isReportSafe(report)
    ).count(true);
    console.log(ans);
    return ans;
};
export const part2 = (lines: string[]): number => {
    // Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.
    console.log(lines);
    const ans = lines.map((line) => parseReport(line)).map((report) => {

        if (isReportSafe(report)) return true
        let found = false
        report.forEach((level, i) => {
            console.log(level)
            const myreport = [...report]
            myreport.splice(i, 1)
            console.log('newreport', level, myreport)
            if (isReportSafe(myreport)) found = true
        })
        return found
    }
    ).count(true);
    console.log(ans);
    return ans;
};

function d02(input: string): number[] {
    const lines = input.trim().split("\n");
    return [
        part1(lines),
        part2(lines),
    ];
}

export default d02;
