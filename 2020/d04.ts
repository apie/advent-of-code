import "./util.ts";
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
const validateFieldValue = (
  fieldName: keyof Passport,
  fieldValue: string | number,
): boolean => {
  //console.log(fieldName);
  switch (fieldName) {
    case "byr":
      return Number(fieldValue).between(1920, 2002);
    case "iyr":
      return Number(fieldValue).between(2010, 2020);
    case "eyr":
      return Number(fieldValue).between(2020, 2030);
    case "hgt":
      if (typeof fieldValue !== "string") return false;
      if (fieldValue.match(/^\d{3}cm$/)) {
        return Number(fieldValue.match(/^\d{3}/)).between(150, 193);
      } else if (fieldValue.match(/^\d{2}in$/)) {
        return Number(fieldValue.match(/^\d{2}/)).between(59, 76);
      } else return false;
    case "hcl":
      if (typeof fieldValue !== "string") return false;
      return !!fieldValue.match(/^#[0-9a-f]{6}$/);
    case "ecl":
      if (typeof fieldValue !== "string") return false;
      return ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"].includes(
        fieldValue,
      );
    case "pid":
      if (typeof fieldValue !== "string") return false;
      return !!fieldValue.match(/^[0-9]{9}$/);
    default:
      throw Error("Unknown field");
  }
};

const validatePassport = (
  passport: Passport,
  shouldValidateFieldValue: boolean,
): boolean => {
  // console.log(passport);
  let valid = true;
  for (const key of passportFields) {
    if (!valid) continue;
    if (!(key in passport)) valid = false;
    else if (
      shouldValidateFieldValue &&
      !validateFieldValue(
        key as keyof Passport,
        passport[key as keyof Passport] || "",
      )
    ) valid = false;
  }
  return valid;
};

const buildPassport = (passportString: string): Passport => {
  const pairs = passportString.split("\n").map((passportLine) =>
    passportLine.split(" ")
  )
    .flat(1);
  return Object.fromEntries(pairs.map((pair) => pair.split(":")));
};

const solution = (passportStrings: string[], validate: boolean): number => {
  return passportStrings.map((passportString) =>
    validatePassport(buildPassport(passportString), validate)
  ).sum();
};

export const part1 = (passportStrings: string[]): number =>
  solution(passportStrings, false);
export const part2 = (passportStrings: string[]): number =>
  solution(passportStrings, true);

function d04(input: string): number[] {
  const lines = input.trim().split("\n\n");
  return [
    part1(lines),
    part2(lines),
  ];
}

export default d04;
