type Passport = {
    byr: number;
    iyr: number;
    eyr: number;
    hgt: string;
    hcl: string;
    ecl: string;
    pid: number;
    cid?: number;
};
const passportFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];

const validatePassport = (passport: Passport): boolean => {
    console.log(passport);
    let valid = true;
    for (const key of passportFields) {
        if (!(key in passport)) {
            valid = false;
        }
    }
    console.log(`Valid: ${valid}`);
    return valid;
};
const buildPassport = (pairs: string[]): Passport => {
    // let pp = {}
    // console.log(pairs);
    return Object.fromEntries(pairs.map((pair) => pair.split(":")));
};
export const part1 = (lines: string[]): number => {
    let numValidPassports = 0;
    let pp: string[] = [];
    lines.forEach((line, i) => {
        // line.split(' ').forEach((pair) => pp[pp.length] = pair)
        pp = pp.concat(line.split(" "));
        if ((line == "") || (i === lines.length - 1)) {
            pp.pop(); // Remove last, empty entry
            if (validatePassport(buildPassport(pp))) numValidPassports += 1;
            pp = [];
        }
    });
    return numValidPassports;
};
export const part2 = (lines: string[]): number => {
    return -1;
};

function d04(input: string): number[] {
    const lines = input.trim().split("\n");

    return [
        part1(lines),
        part2(lines),
    ];
}

export default d04;
