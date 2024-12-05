import d01 from "./d01.ts";
import d02 from "./d02.ts";
import d03 from "./d03.ts";
import d05 from "./d05.ts";

const [day] = Deno.args;
if (!day) {
    console.error("Provide day as argument");
    Deno.exit(1);
}

const startTime = Date.now();
const fileName = `d${("0" + day).slice(-2)}.input`;
const text = await Deno.readTextFile(fileName);
let answers;
switch (day) {
    case "1":
        answers = d01(text);
        break;
    case "2":
        answers = d02(text);
        break;
    case "3":
        answers = d03(text);
        break;
    case "5":
        answers = d05(text);
        break;
    default:
        console.error("Unknown day");
        Deno.exit(1);
}
console.log("DAY", day, "solution part1:", answers[0]);
console.log("DAY", day, "solution part2:", answers[1]);
console.log("Solution took", Date.now() - startTime, "ms");
