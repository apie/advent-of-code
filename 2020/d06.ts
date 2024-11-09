import "./util.ts";

const countYes = (group: string): number => {
    const uniqueChars = new Set(group.replaceAll("\n", ""));
    return uniqueChars.size;
};

export const part1 = (groups: string[]): number =>
    groups.map((group) => countYes(group)).sum();

const countAllYes = (group: string): number => {
    console.log();
    console.log(group);
    const answers = group.replaceAll("\n", "").split("");
    const groupsize = group.split("\n").length;
    const uniqueChars = new Set(group.replaceAll("\n", ""));
    let answer = 0;
    uniqueChars.forEach((char) => {
        const c = answers.count(char);
        console.log("charcount", char, c);
        if (c === groupsize) answer += 1;
    });
    console.log("answer", answer);
    return answer;
};

export const part2 = (groups: string[]): number =>
    groups.map((group) => countAllYes(group)).sum();

function d06(input: string): number[] {
    const lines = input.trim().split("\n\n");
    return [
        part1(lines),
        part2(lines),
    ];
}

export default d06;
