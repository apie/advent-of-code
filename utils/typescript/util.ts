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
            this.shift(),
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

declare global {
    interface Array<T> {
        sum(): number;
        prod(): number;
        max(): number;
        count(c: string | number | boolean): number;
    }
    interface Number {
        between(a: Number, b: Number): boolean;
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
    console.debug(...t);
}
