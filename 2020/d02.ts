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
function checkPasswordPart1(
    word: string,
    letter: string,
    posOne: number,
    posTwo: number,
): boolean {
    let numMatched = 0;
    const passwordArray = word.split("");
    let letterIndex = -1;
    while (numMatched <= passwordArray.length) {
        letterIndex = passwordArray.indexOf(letter);
        if (letterIndex > -1) {
            passwordArray[letterIndex] = ".";
            numMatched += 1;
        } else {
            break;
        }
    }
    if (numMatched > Number(posTwo)) return false;
    if (numMatched < Number(posOne)) return false;
    return true;
}

function checkPasswordPart2(
    word: string,
    letter: string,
    posOne: number,
    posTwo: number,
): boolean {
    return Boolean(
        Number(word[posOne - 1] === letter) ^
            Number(word[posTwo - 1] === letter),
    );
}
export function solution(
    input: string,
    checkPasswordFunction: (
        word: string,
        letter: string,
        posOne: number,
        posTwo: number,
    ) => boolean,
): number {
    const passwords = input.trim().split("\n");
    return passwords.filter((pw) => pw[0].match(/\d/)).map((pw) => {
        const parsedPassword = parsePassword(pw);
        if (!parsedPassword.groups) return false;
        const posOne = Number(parsedPassword.groups.from);
        const posTwo = Number(parsedPassword.groups.to);
        const letter = parsedPassword.groups.letter;
        const word = parsedPassword.groups.hay;
        return checkPasswordFunction(word, letter, posOne, posTwo);
    }).filter((pwOK) => pwOK === true).length;
}

export const part1 = (input: string): number =>
    solution(input, checkPasswordPart1);
export const part2 = (input: string): number =>
    solution(input, checkPasswordPart2);

function d02(d02_input: string): number[] {
    return [
        part1(d02_input),
        part2(d02_input),
    ];
}

export default d02;
