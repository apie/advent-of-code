import "./util.ts";
import { p } from "./util.ts";

const findLargestPossibleJoltage = (bank: string): number => {
    p(bank);
    let battery1, battery2;
    // find highest battery
    const highest = Number(bank.split("").max());
    const index = bank.indexOf(highest.toString());
    p(index, ":", highest);
    // if highest is last battery, partition and use highest battery from first part as first digit and from second part as second digit
    if (index == bank.length - 1) {
        p("highest is last battery");
        battery2 = highest;
        const firstPart = bank.substring(0, index);
        // p(firstPart);
        battery1 = Number(firstPart.split("").max());
    } // otherwise, do other way around
    else {
        battery1 = highest;
        const secondPart = bank.substring(index + 1);
        // p(secondPart);
        battery2 = Number(secondPart.split("").max());
    }
    p("battery1", battery1, "battery2", battery2);
    const joltage = battery1 * 10 + battery2;
    p("joltage", joltage);
    return joltage;
};
export const part1 = (banks: string[]): number => {
    console.log(
        "Part 1: Find largest possible joltage each bank can produce and sum it.",
    );
    return banks.map((bank) => findLargestPossibleJoltage(bank)).sum();
};
export const part2 = (banks: string[]): number => {
    return 0;
};

function* d03(input: string): Generator<number> {
    console.log("Day 3: Lobby");
    const lines = input.trim().split("\n");
    yield part1(lines);
    yield part2(lines);
}

export default d03;
