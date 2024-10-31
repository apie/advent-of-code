import { sum } from "./util.ts";
function parsePassword(password: string): RegExpMatchArray {
    // console.log(password);
    const parsedPassword = password.match(
        /(?<from>\d+)-(?<to>\d+) (?<letter>\w): (?<hay>\w+)/,
    );
    if (!parsedPassword?.groups) {
        throw Error("unknown line found");
    }
    return parsedPassword;
}
function checkPassword(password: string): boolean {
    // console.log(password);
    const parsedPassword = password.match(
        /(?<from>\d+)-(?<to>\d+) (?<letter>\w): (?<hay>\w+)/,
    );
    if (!parsedPassword?.groups) {
        throw Error("unknown line found");
    }
    let numMatched = 0;
    const passwordArray = parsedPassword.groups.hay.split("");
    let letterIndex = -1;
    while (numMatched <= passwordArray.length) {
        letterIndex = passwordArray.indexOf(parsedPassword.groups.letter);
        if (letterIndex > -1) {
            passwordArray[letterIndex] = ".";
            numMatched += 1;
        } else {
            break;
        }
    }
    if (numMatched > Number(parsedPassword.groups.to)) return false;
    if (numMatched < Number(parsedPassword.groups.from)) return false;
    return true;
}
export function part1(d02_input: string): number {
    const passwords = d02_input.trim().split("\n");
    return passwords.filter((pw) => pw[0].match(/\d/)).map((pw) =>
        checkPassword(pw)
    ).reduce(
        (total: number, result: boolean) => total += Number(result),
        0,
    );
}
function checkPasswordPart2(
    word: string,
    letter: string,
    posOne: number,
    posTwo: number,
) {
    return Boolean(
        Number(word[posOne - 1] === letter) ^
            Number(word[posTwo - 1] === letter),
    );
}

export function part2(d02_input: string): number {
    const passwords = d02_input.trim().split("\n");
    return sum(
        passwords.filter((pw) => pw[0].match(/\d/)).map((pw) => {
            const parsedPassword = parsePassword(pw);
            if (!parsedPassword.groups) return false;
            const posOne = Number(parsedPassword.groups.from);
            const posTwo = Number(parsedPassword.groups.to);
            const letter = parsedPassword.groups.letter;
            const word = parsedPassword.groups.hay;
            return checkPasswordPart2(word, letter, posOne, posTwo);
        }),
    );
}
function d02(d02_input: string): number[] {
    return [part1(d02_input), part2(d02_input)];
}

export default d02;
