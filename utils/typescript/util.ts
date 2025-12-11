import { assert } from "jsr:@std/assert@1.0.11";
import memoize from "jsr:@korkje/memz@0.2.1";

export const isRunningInTest = memoize((): boolean => {
    const stack = new Error().stack;
    return stack?.includes("test") || stack?.includes("Test") || false;
});
Object.defineProperty(Array.prototype, "sum", {
    enumerable: false,
    value: function () {
        return this.reduce(
            (total: number, item: number | boolean) => total += Number(item),
            0,
        );
    },
});
Object.defineProperty(Array.prototype, "prod", {
    enumerable: false,
    value: function () {
        return this.reduce(
            (total: number, item: number | boolean) => total *= Number(item),
            1,
        );
    },
});
Object.defineProperty(Array.prototype, "max", {
    enumerable: false,
    value: function () {
        return this.reduce(
            (highest: number, item: number) => item > highest ? item : highest,
            this[0],
        );
    },
});
Object.defineProperty(Array.prototype, "min", {
    enumerable: false,
    value: function () {
        return this.reduce(
            (lowest: number, item: number) => item < lowest ? item : lowest,
            this[0],
        );
    },
});
Object.defineProperty(Array.prototype, "count", {
    enumerable: false,
    value: function (c: string | number | boolean) {
        return this.reduce(
            (total: number, item: string | number | boolean) =>
                item === c ? total += 1 : total,
            0,
        );
    },
});
Number.prototype.between = function (a, b) {
    return this >= a && this <= b;
};
String.prototype.replaceCharAt = function (
    position: number,
    char: string,
): string {
    assert(char.length === 1, "char must be only one char long");
    const charArray = this.split("");
    charArray[position] = char;
    return charArray.join("");
};
declare global {
    interface Array<T> {
        sum(): number;
        prod(): number;
        /**
         * Returns the highest number in the array.
         */
        max(): number;
        /**
         * Returns the lowest number in the array.
         */
        min(): number;
        count(c: string | number | boolean): number;
    }
    interface Number {
        between(a: Number, b: Number): boolean;
    }
    interface String {
        /**
         * Replaces the character at the provided position with the provided character.
         */
        replaceCharAt(position: Number, char: string): string;
    }
}

export function* combinations2(
    array1: number[],
    array2: number[],
): Generator<number[]> {
    let it = 0;
    for (let index1 = 0; index1 < array1.length; index1++) {
        for (let index2 = 0; index2 < array2.length; index2++) {
            if (index1 !== index2) {
                yield [
                    array1[index1],
                    array2[index2],
                ];
                it++;
            }
        }
    }
}

export function* combinations3(
    array1: number[],
    array2: number[],
    array3: number[],
): Generator<number[]> {
    let it = 0;
    for (let index1 = 0; index1 < array1.length; index1++) {
        for (let index2 = 0; index2 < array2.length; index2++) {
            for (let index3 = 0; index3 < array3.length; index3++) {
                if ((index1 !== index2) && (index1 !== index3)) {
                    yield [
                        array1[index1],
                        array2[index2],
                        array3[index3],
                    ];
                    it++;
                }
            }
        }
    }
}

// deno-lint-ignore no-explicit-any
export function p(...t: any[]) {
    if (isRunningInTest()) console.debug(...t);
}

export class Point {
    x: number;
    y: number;
    constructor(x: number, y: number) {
        this.x = x;
        this.y = y;
    }
    getUniqueKey() {
        return `${this.x},${this.y}`;
    }
    getAdjacent(): Point[] {
        return [
            new Point(this.x - 1, this.y), //above
            new Point(this.x - 1, this.y + 1), //right above
            new Point(this.x, this.y + 1),
            new Point(this.x + 1, this.y + 1),
            new Point(this.x + 1, this.y),
            new Point(this.x + 1, this.y - 1),
            new Point(this.x, this.y - 1),
            new Point(this.x - 1, this.y - 1),
        ];
    }
}

export const sortPoints = (pointArray: Point[]): Point[] =>
    pointArray.sort((a, b) => (a.y * 10_000 + a.x) - (b.y * 10_000 + b.x));

/**
 * Grid class that uses a string array as constructor, and also uses this format internally.
 */
export class Grid {
    g: string[];
    constructor(g: string[]) {
        // assign copy of g
        this.g = Object.assign([], g);
    }
    size(): number[] {
        return [this.g.length, this.g[0].length];
    }
    lines() {
        return this.g;
    }
    _dbg_print() {
        p("_print");
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
    _dbg_printv(
        po?: Point[] | MapIterator<Point>,
        char?: string,
        invert?: boolean,
    ) {
        // Print the grid values,
        // Optionally providing points that should be highlighted in bold red.
        // Optionally providing the char that should be used for the highlighted positions.
        if (po && invert) {
            po = Array.from(po).map((poi) => new Point(poi.y, poi.x));
        }
        p("_printv");
        const [xlen, ylen] = this.size();
        let h = "  ";
        for (let y = 0; y < ylen; y++) {
            h += " " + y;
        }
        p(h);
        for (let x = 0; x < xlen; x++) {
            let row = x + "";
            if (x < 10) row += " ";
            for (let y = 0; y < ylen; y++) {
                const val = " " + this.g[x][y];
                if (po?.find((pt) => pt.x === x && pt.y === y)) {
                    row += `\x1b[1m\x1b[31m${char ? " " + char : val}\x1b[0m`;
                } else row += val;
            }
            p(row);
        }
        p();
    }
    _dbg_printdiag(counter: number) {
        p("_printdiag");
        const [xlen, ylen] = this.size();
        assert(counter < xlen, "Counter out of range");
        assert(counter > -ylen, "Counter out of range");
        for (let x = 0; x < xlen; x++) {
            let row = "";
            for (let y = 0; y < ylen; y++) {
                if (x - y === counter) row += `${x},${y} `;
                else row += " ,  ";
            }
            p(row);
        }
        p();
    }
    _dbg_printrotated() {
        p("_printrotated");
        const [xlen, ylen] = this.size();
        for (let x = 0; x < xlen; x++) {
            let row = "";
            for (let y = 0; y < ylen; y++) {
                row += `${ylen - 1 - y},${x} `;
            }
            p(row);
        }
        p();
    }
    isFree(p: Point, freeChar: string = "."): boolean {
        return this.g[p.x][p.y] === freeChar;
    }
    isBlocked(p: Point, blockChar: string = "@"): boolean {
        return this.g[p.x][p.y] === blockChar;
    }
    /**
     * Walks grid, column first.
     */
    *walkGrid(): Generator<[Point, string]> {
        const [xlen, ylen] = this.size();
        for (let x = 0; x < xlen; x++) {
            for (let y = 0; y < ylen; y++) {
                yield [new Point(x, y), this.g[x][y]];
            }
        }
    }
    /**
     * Walks grid, row first
     */
    *walkGridRowFirst(): Generator<[Point, string]> {
        const [xlen, ylen] = this.size();
        for (let y = 0; y < ylen; y++) {
            for (let x = 0; x < xlen; x++) {
                yield [new Point(x, y), this.g[x][y]];
            }
        }
    }
    onGrid(p: Point): boolean {
        const [xlen, ylen] = this.size();
        return p.x.between(0, xlen - 1) && p.y.between(0, ylen - 1);
    }
    replaceCharAt(position: Point, char: string): void {
        this.g[position.x] = this.g[position.x].replaceCharAt(position.y, char);
    }
}
