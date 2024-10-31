export function sum(arr: number[] | boolean[]): number {
    return arr.reduce(
        (total: number, item: number | boolean) => total += Number(item),
        0,
    );
}
