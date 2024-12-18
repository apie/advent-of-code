import { assert } from "jsr:@std/assert/assert";
import "./util.ts";
import { Grid, p, Point } from "./util.ts";

class WordGrid extends Grid {
    _getrotated(): string[] {
        const lines = [];
        const [xlen, ylen] = this.size();
        for (let x = 0; x < xlen; x++) {
            let line = "";
            for (let y = 0; y < ylen; y++) {
                line += this.g[ylen - 1 - y][x];
            }
            lines[lines.length] = line;
        }
        return lines;
    }
    rotate90() {
        p("\n~~rotating");
        this.g = this._getrotated();
    }
    _getdiag(counter: number): string {
        const [xlen, ylen] = this.size();
        assert(counter < xlen, "Counter out of range");
        assert(counter > -ylen, "Counter out of range");
        let rows = "";
        for (let x = 0; x < xlen; x++) {
            let row = "";
            for (let y = 0; y < ylen; y++) {
                if (x - y === counter) row += `${this.g[x][y]}`;
            }
            rows += row;
        }
        return rows;
    }
    getDiagLines(): string[] {
        const [xlen, ylen] = this.size();
        const lines = [];
        for (let counter = -ylen + 1; counter < xlen; counter++) {
            lines[lines.length] = this._getdiag(counter);
        }
        return lines;
    }
}

const countXMAS = (lines: string[]): number =>
    lines.map((line) => line.match(/XMAS/g)?.length).filter((
        result,
    ) => result !== undefined).sum();

export const part1 = (lines: string[]): number => {
    const gr = new WordGrid(lines);

    const myg = gr.g;
    [...Array(4).keys()].forEach((_direction) => gr.rotate90());
    assert(myg.join(".") === gr.g.join("."), "rotated 360 should be equal");

    const xmascounts = [...Array(4).keys()].map((_direction) => {
        gr.rotate90();
        return countXMAS(gr.lines()) + countXMAS(gr.getDiagLines());
    });
    p(xmascounts, "totaal:", xmascounts.sum());
    return xmascounts.sum();
};

const countXMASpt2 = (lines: string[]): number => {
    return lines.map((line, i) => {
        return Array.from(line.matchAll(/A/g)).map((m) => {
            const found = lines[i - 1]?.[m.index - 1] === "M" &&
                lines[i + 1]?.[m.index - 1] === "M" &&
                lines[i - 1]?.[m.index + 1] === "S" &&
                lines[i + 1]?.[m.index + 1] === "S";
            // debug output if testinput is being used
            if (found && lines[0].length < 11) {
                p("match found (A) at", i, m.index);
                new Grid(lines)._dbg_printv([
                    new Point(i, m.index),
                    new Point(i - 1, m.index - 1),
                    new Point(i + 1, m.index - 1),
                    new Point(i - 1, m.index + 1),
                    new Point(i + 1, m.index + 1),
                ]);
            }
            return found;
        }).sum();
    }).filter((
        result,
    ) => result !== undefined).filter((
        result,
    ) => !Number.isNaN(result)).sum();
};
export const part2 = (lines: string[]): number => {
    const gr = new WordGrid(lines);
    const xmascounts = [...Array(4).keys()].map((_direction) => {
        gr.rotate90();
        // gr._dbg_printv();
        return countXMASpt2(gr.lines());
    });
    p("\n\n-->", xmascounts, "totaal:", xmascounts.sum());
    return xmascounts.sum();
};

function d04(input: string): number[] {
    const lines = input.trim().split("\n");
    return [
        part1(lines),
        part2(lines),
    ];
}

export default d04;
