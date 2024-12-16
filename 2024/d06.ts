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
        this.dir = direction.UP;
    }
    _parseInitialPos() {
        // initial pos is marked in the grid with ^
        const x = this.g.findIndex((row) => row.indexOf("^") > -1);
        const y = this.g[x].indexOf("^");
        return new Point(x, y);
    }
    _dbg_printpos() {
        this._dbg_printv([this.pos], "🯆");
        p("pos", this.pos);
        p("moving", this.dir);
        p("char at pos", this.getCharAtPos());
        p("char in front", this.getCharInFrontOfPos());
        p("--------------");
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
    move() {
        if (this.getCharInFrontOfPos() === "#") this.turnRight();
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
        p("~~turning");
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
    }
    inGrid(): boolean {
        const [x, y] = this.size();
        return this.pos.x.between(0, x) && this.pos.y.between(0, y);
    }
}

export const part1 = (lines: string[]): number => {
    const l = new Lab(lines);
    l._dbg_printpos();

    const visited = new Set();
    visited.add(`${l.pos.x},${l.pos.y}`);
    const size = l.size();
    while (l.inGrid()) {
        try {
            l.move();
            visited.add(`${l.pos.x},${l.pos.y}`);
            if (size[0] < 11) l._dbg_printpos();
        } catch (error) {
            break;
        }
    }
    return visited.size;
};
export const part2 = (lines: string[]): number => {
    return 0;
};

function d06(input: string): number[] {
    const lines = input.trim().split("\n");
    return [
        part1(lines),
        part2(lines),
    ];
}

export default d06;
