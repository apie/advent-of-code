import "./util.ts";
import { Grid, p, Point } from "./util.ts";

enum direction {
    UP = "up",
    DOWN = "down",
    LEFT = "left",
    RIGHT = "right",
}
class Lab extends Grid {
    pos: Point;
    dir: direction;
    constructor(g: string[]) {
        super(g);
        this.pos = this._parseInitialPos();
        this.g[this.pos.x] = this.g[this.pos.x].replaceCharAt(this.pos.y, ".");
        this.dir = direction.UP;
    }
    _parseInitialPos() {
        // initial pos is marked in the grid with ^
        const x = this.g.findIndex((row) => row.indexOf("^") > -1);
        const y = this.g[x].indexOf("^");
        return new Point(x, y);
    }
    override _dbg_printv(po?: Point[]) {
        let char = "";
        switch (this.dir) {
            case direction.UP:
                char = "↑";
                break;
            case direction.DOWN:
                char = "↓";
                break;
            case direction.LEFT:
                char = "←";
                break;
            case direction.RIGHT:
                char = "→";
                break;
        }
        super._dbg_printv(po, char);
    }
    _dbg_printpos() {
        this._dbg_printv([this.pos]);
        p(
            "pos",
            this.pos,
            "moving",
            this.dir + ".",
            "char at pos:",
            this.getCharAtPos(),
            "char in front:",
            this.getCharInFrontOfPos(),
        );
        p();
    }
    getCharAtPos() {
        return this.g[this.pos.x][this.pos.y];
    }
    getCharInFrontOfPos() {
        //in front: 1 in front depending on direction
        switch (this.dir) {
            case direction.UP:
                return this.g[this.pos.x - 1][this.pos.y];
            case direction.DOWN:
                return this.g[this.pos.x + 1][this.pos.y];
            case direction.LEFT:
                return this.g[this.pos.x][this.pos.y - 1];
            case direction.RIGHT:
                return this.g[this.pos.x][this.pos.y + 1];
        }
    }
    positionBlocked() {
        return (this.getCharInFrontOfPos() === "#") ||
            (this.getCharInFrontOfPos() === "O");
    }
    move() {
        while (this.positionBlocked()) this.turnRight();
        switch (this.dir) {
            case direction.UP:
                this.pos.x -= 1;
                break;
            case direction.DOWN:
                this.pos.x += 1;
                break;
            case direction.LEFT:
                this.pos.y -= 1;
                break;
            case direction.RIGHT:
                this.pos.y += 1;
                break;
        }
    }
    turnRight() {
        switch (this.dir) {
            case direction.UP:
                this.dir = direction.RIGHT;
                break;
            case direction.DOWN:
                this.dir = direction.LEFT;
                break;
            case direction.LEFT:
                this.dir = direction.UP;
                break;
            case direction.RIGHT:
                this.dir = direction.DOWN;
                break;
        }
        if (this.size()[0] < 11) this._dbg_printpos();
    }
    inGrid(): boolean {
        const [x, y] = this.size();
        return this.pos.x.between(0, x) && this.pos.y.between(0, y);
    }
    getKey(withDir: boolean = false): string {
        const key = `${this.pos.x},${this.pos.y}`;
        if (withDir) return key + `,${this.dir}`;
        return key;
    }
    getKeyWithDir(): string {
        return this.getKey(true);
    }
}

export const getVisitedLocations = (
    lines: string[],
): Set<string> => {
    const l = new Lab(lines);
    if (l.size()[0] < 11) l._dbg_printpos();

    const visited: Set<string> = new Set();
    visited.add(l.getKey());
    while (l.inGrid()) {
        try {
            l.move();
            visited.add(l.getKey());
        } catch (_error) {
            break; // moved out of grid
        }
    }
    return visited;
};

export const part1 = (lines: string[]): number =>
    getVisitedLocations(lines).size;

export const causesLoop = (lines: string[]): boolean => {
    const l = new Lab(lines);
    const visited = new Set();
    visited.add(l.getKeyWithDir());
    while (l.inGrid()) {
        try {
            l.move();
            if (visited.has(l.getKeyWithDir())) {
                // "Already visited ";
                return true;
            }
            visited.add(l.getKeyWithDir());
        } catch (_error) {
            break; // moved out of grid
        }
    }
    return false;
};
export const part2 = (lines: string[]): number => {
    // Locations where we can drop things, based on part1. Using a copy of lines.
    const visitedLocations = getVisitedLocations(Object.assign([], lines));
    let numberOfDropLocations = 0;
    const dropLocations = Array.from(visitedLocations).map((a) =>
        a.split(",").map((c) => Number(c))
    );
    // Remove start pos from the list (per instruction)
    dropLocations.shift();
    dropLocations.forEach((dl) => {
        // Drop object 'O' on each droplocation
        const clonedLines: string[] = Object.assign([], lines);
        const [row, col] = dl;
        clonedLines[row] = clonedLines[row].replaceCharAt(col, "O");
        if (causesLoop(clonedLines)) numberOfDropLocations++;
    });
    return numberOfDropLocations;
};

function d06(input: string): number[] {
    const lines = input.trim().split("\n");
    return [
        part1(lines),
        part2(lines),
    ];
}

export default d06;
