import d01 from "./d01.ts";
import d02 from "./d02.ts";
import d03 from "./d03.ts";
import d04 from "./d04.ts";
import d05 from "./d05.ts";
import d06 from "./d06.ts";
import d07 from "./d07.ts";
import d08 from "./d08.ts";
import d09 from "./d09.ts";

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
    case "4":
        answers = d04(text);
        break;
    case "5":
        answers = d05(text);
        break;
    case "6":
        answers = d06(text);
        break;
    case "7":
        answers = d07(text);
        break;
    case "8":
        answers = d08(text);
        break;
    case "9":
        answers = d09(text);
        break;
    default:
        console.error("Unknown day");
        Deno.exit(1);
}
answers.forEach((answer, i) =>
    console.log("Day", day, "solution part", i + 1, ":", answer)
);
console.log("Solution took", Date.now() - startTime, "ms");
