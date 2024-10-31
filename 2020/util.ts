export const sum = (arr: number[] | boolean[]): number =>
    arr.reduce(
        (total: number, item: number | boolean) => total += Number(item),
        0,
    );

export const combinations = (
    array1: number[],
    array2: number[],
): number[][] => {
    let it = 0;
    const combinations = [];
    for (let index1 = 0; index1 < array1.length; index1++) {
        for (let index2 = 0; index2 < array2.length; index2++) {
            if (index1 !== index2) {
                combinations[it] = [
                    array1[index1],
                    array2[index2],
                ];
                it++;
            }
        }
    }
    return combinations;
};
