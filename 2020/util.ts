export const sum = (arr: number[] | boolean[]): number =>
    arr.reduce(
        (total: number, item: number | boolean) => total += Number(item),
        0,
    );

export const prod = (arr: number[]): number =>
    arr.reduce(
        (total: number, item: number) => total *= item,
        arr.pop() || 0,
    );

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
