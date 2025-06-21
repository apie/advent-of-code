import "./util.ts";
import { p, isRunningInTest } from "./util.ts";

interface ifilesystem {
    pos: number;
    type: 'file' | 'free';
    id?: number;
    len: number;
}
const checksum = (filemap: Map<number, ifilesystem>): number => Array.from(filemap.values().filter((curobj) => curobj.type === "file").map((curobj) => {
    let tot = 0
    for (let plen = 0; plen < curobj.len; plen++) tot += curobj.id! * (curobj.pos + plen);
    return tot;
})).sum()

const compact = (filemap: Map<number, ifilesystem>): void => {
    p('compacting..')
    filemap.values().forEach((curobj) => {
        let keepgoing = true
        while (keepgoing) {
            const lastobjpos = Array.from(filemap.keys()).max()
            if (curobj.pos >= lastobjpos) return;
            p('lastobjpos', lastobjpos)
            p('curobj', curobj)
            const lastobj = filemap.get(lastobjpos);
            if (!lastobj) throw Error;
            if (lastobj.type === 'free') {
                filemap.delete(lastobjpos);
                continue
            }
            p('lastobj len', lastobj.len)
            if (curobj.type === 'free') {
                p('free obj found')
                if (lastobj.len == curobj.len) {
                    // put lastobj here
                    filemap.set(curobj.pos, {
                        pos: curobj.pos,
                        id: lastobj.id,
                        type: lastobj.type,
                        len: lastobj.len,
                    })
                    // update lastobj
                    filemap.delete(lastobjpos);
                    keepgoing = false
                } else if (lastobj.len < curobj.len) {
                    // put lastobj here
                    filemap.set(curobj.pos, {
                        pos: curobj.pos,
                        id: lastobj.id,
                        type: lastobj.type,
                        len: lastobj.len,
                    })
                    // update lastobj
                    filemap.delete(lastobjpos);
                    curobj.pos = curobj.pos + lastobj.len
                    curobj.len = curobj.len - lastobj.len
                } else {
                    // put part of lastobj here
                    filemap.set(curobj.pos, {
                        pos: curobj.pos,
                        id: lastobj.id,
                        type: lastobj.type,
                        len: curobj.len,
                    })
                    // update lastobj
                    filemap.set(lastobj.pos, {
                        pos: lastobj.pos,
                        id: lastobj.id,
                        type: lastobj.type,
                        len: lastobj.len - curobj.len,
                    })
                    keepgoing = false
                }
            } else { keepgoing = false }
            printfs(filemap)
        }
    })
    p('done compacting')
}
const compactWholeFiles = (filemap: Map<number, ifilesystem>): void => {
    p('compacting..')
    Array.from(filemap.values().filter((curobj) => curobj.type === 'file')).sort((a, b) => -1 * (a?.id || 0) + (b?.id || 0)).forEach((lastobj) => {
        //find free space
        const freeobj = Array.from(filemap.values().filter((curobj) => curobj.type === 'free')).sort((a, b) => a.pos - b.pos).find((curobj) => curobj.len >= lastobj.len)
        if (!freeobj) return
        if (freeobj.pos > lastobj.pos) return;
        p('--> moving', lastobj.id)
        // move lastobj to position of freeobj
        filemap.set(freeobj.pos, {
            pos: freeobj.pos,
            id: lastobj.id,
            type: lastobj.type,
            len: lastobj.len,
        })
        // update lastobj. dont delete because it might not be the last obj
        filemap.set(lastobj.pos, {
            pos: lastobj.pos,
            type: 'free',
            len: lastobj.len,
        });
        if (freeobj.len > lastobj.len) {
            // if needed add new freeobj after our moved obj
            filemap.set(freeobj.pos + lastobj.len, {
                pos: freeobj.pos + lastobj.len,
                type: 'free',
                len: freeobj.len - lastobj.len,
            })
        }
        printfs(filemap)

    })
    p('done compacting')
}
const printfs = (filemap: Map<number, ifilesystem>): void => {
    if (!isRunningInTest()) return;
    let toprint = '';
    let curpos = 0;
    while (true) {
        const curobj = filemap.get(curpos);
        if (!curobj) break;
        let pchar = '';
        switch (curobj.type) {
            case 'file':
                pchar = String(curobj.id);
                break;
            case 'free':
                pchar = '.';
                break;

        }
        for (let plen = 0; plen < curobj.len; plen++) toprint += pchar;
        curpos += curobj.len;
    }
    p(toprint)
}
const parsemap = (denseformat: string): Map<number, ifilesystem> => {
    const filesystemmap = new Map<number, ifilesystem>();
    let id = 0;
    let pos = 0;
    denseformat.split('').map((c) => Number(c)).forEach((n, i) => {
        if (i % 2 == 0) {
            filesystemmap.set(pos, {
                pos: pos,
                type: 'file',
                id: id,
                len: n,
            })
            id++;
        } else {
            filesystemmap.set(pos, {
                pos: pos,
                type: 'free',
                len: n,
            })
        }
        pos += n
    });
    return filesystemmap;
}
export const part1 = (lines: string[]): number => {
    p(lines[0])
    const filesystemmap = parsemap(lines[0])
    printfs(filesystemmap)
    compact(filesystemmap)
    printfs(filesystemmap)
    return checksum(filesystemmap);
};
export const part2 = (lines: string[]): number => {
    p(lines[0])
    const filesystemmap = parsemap(lines[0])
    printfs(filesystemmap)
    compactWholeFiles(filesystemmap)
    printfs(filesystemmap)
    return checksum(filesystemmap);
};

function d09(input: string): number[] {
    const lines = input.trim().split("\n");
    return [
        part1(lines),
        part2(lines),
    ];
}

export default d09;
