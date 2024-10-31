export const sum = (arr: number[] | boolean[]): number =>
    arr.reduce(
        (total: number, item: number | boolean) => total += Number(item),
        0,
    );
