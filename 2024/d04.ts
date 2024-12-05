import { assert } from "jsr:@std/assert/assert";
import "./util.ts";
import { p } from "./util.ts";

class Grid {
    g: string[];
    constructor(g: string[]) {
        this.g = g;
    }
    size(): number[] {
        return [this.g.length, this.g[0].length];
    }
    lines() {
        return this.g;
    }
    _dbg_print() {
        console.debug("_print");
        const [xlen, ylen] = this.size();
        for (let x = 0; x < xlen; x++) {
            let row = "";
            for (let y = 0; y < ylen; y++) {
                row += `${x},${y} `;
            }
            p(row);
        }
        p();
    }
    _dbg_printdiag(counter: number) {
        console.debug("_printdiag");
        const [xlen, ylen] = this.size();
        assert(counter < xlen, "Counter out of range");
        assert(counter > -ylen, "Counter out of range");
        for (let x = 0; x < xlen; x++) {
            let row = "";
            for (let y = 0; y < ylen; y++) {
                // p('xy', x, y);
                if (x - y === counter) row += `${x},${y} `;
                else row += " ,  ";
            }
            p(row);
        }
        p();
    }
    _dbg_printrotated() {
        console.debug("_printrotated");
        const [xlen, ylen] = this.size();
        for (let x = 0; x < xlen; x++) {
            let row = "";
            for (let y = 0; y < ylen; y++) {
                // p('xy', x, y);
                row += `${ylen - 1 - y},${x} `;
            }
            p(row);
        }
        p();
    }
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
    const gr = new Grid(lines);

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
export const part2 = (lines: string[]): number => {
    return 0;
};

function d04(input: string): number[] {
    const lines = input.trim().split("\n");
    return [
        part1(lines),
        part2(lines),
    ];
}

export default d04;
