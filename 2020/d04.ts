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
  let val = -1;
  switch (fieldName) {
    case "byr":
      val = Number(fieldValue);
      if (val < 1920) return false;
      if (val > 2002) return false;
      break;
    case "iyr":
      val = Number(fieldValue);
      if (val < 2010) return false;
      if (val > 2020) return false;
      break;
    case "eyr":
      val = Number(fieldValue);
      if (val < 2020) return false;
      if (val > 2030) return false;
      break;
    case "hgt":
      if (typeof fieldValue !== "string") return false;
      if (fieldValue.match(/^\d{3}cm$/)) {
        const hgtCm = Number(fieldValue.match(/^\d{3}/));
        if (hgtCm < 150) return false;
        if (hgtCm > 193) return false;
      } else if (fieldValue.match(/^\d{2}in$/)) {
        const hgtIn = Number(fieldValue.match(/^\d{2}/));
        if (hgtIn < 59) return false;
        if (hgtIn > 76) return false;
      } else return false;
      break;
    case "hcl":
      if (typeof fieldValue !== "string") return false;
      if (!fieldValue.match(/^#[0-9a-f]{6}$/)) return false;
      break;
    case "ecl":
      if (typeof fieldValue !== "string") return false;
      if (
        !["amb", "blu", "brn", "gry", "grn", "hzl", "oth"].includes(fieldValue)
      ) return false;
      break;
    case "pid":
      if (typeof fieldValue !== "string") return false;
      if (!fieldValue.match(/^[0-9]{9}$/)) return false;
      break;
  }
  //console.log(fieldName, true);
  return true;
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
