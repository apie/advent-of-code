import d01 from "./d01.ts";
import d02 from "./d02.ts";
import d03 from "./d03.ts";
import d04 from "./d04.ts";

const [day] = Deno.args;
if (!day) {
    console.error("Provide day as argument");
    Deno.exit(1);
}

const startTime = Date.now();
const file = await Deno.open(`d${("0" + day).slice(-2)}.input`, { read: true });
const buf = new Uint8Array(100000);
file.read(buf);
const text = new TextDecoder().decode(buf);
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
    default:
        console.error("Unknown day");
        Deno.exit(1);
}
console.log("DAY", day, "solution part1:", answers[0]);
console.log("DAY", day, "solution part2:", answers[1]);
console.log("Solution took", Date.now() - startTime, "ms");
