#!/usr/bin/env python3
#Print a line when someone from your private leaderboard on adventofcode.com solves a puzzle. Updates at most every 15 minutes since more is not allowed.
#By Apie 2021-12-13

import os
import requests
import json
from datetime import datetime, timedelta, date
from pathlib import Path
from os.path import dirname, abspath
from time import sleep



COOKIE_FILE = dirname(abspath(__file__))+'/../cookie.txt'
with open(COOKIE_FILE) as f:
    COOKIE = f.read().strip()

YEAR = 2021
LEADERBOARD_ID = 380357
STATS_URL = f'https://adventofcode.com/{YEAR}/leaderboard/private/view/{LEADERBOARD_ID}.json' 
FILENAME = Path(dirname(abspath(__file__))+'/cache.txt')

s = requests.session()


def get_from_cache() -> str:
    if not FILENAME.exists():
        return
    if datetime.fromtimestamp(FILENAME.stat().st_mtime)+timedelta(minutes=15) < datetime.now():
        os.remove(FILENAME)
        return
    with open(FILENAME) as f:
        return f.read()

def update_cache():
    r = s.get(STATS_URL, cookies=dict(session=COOKIE), timeout=5)
    r.raise_for_status()
    stats = r.text
    with open(FILENAME, "w") as f:
        f.write(stats)
    return stats

def get_stats():
    return get_from_cache() or update_cache()

def get_done_set(m):
    return {
        'day '+day+' part '+part
        for day, parts in m['completion_day_level'].items()
        for part in parts
    }


if __name__ == '__main__':
    puzzles_done = dict()
    stats = json.loads(get_stats())
    for m_id, m in stats['members'].items():
        name = m['name']
        puzzles_done[name] = get_done_set(m)

    while True:
        sleep(60*1)
        stats = json.loads(get_stats())
        for m_id, m in stats['members'].items():
            done = get_done_set(m)
            name = m['name']
            if len(done) == len(puzzles_done[name]):
                continue # nothing changed
            dt = datetime.now()
            print(f'[{dt.strftime("%Y-%m-%d %H:%M:%S")}] {name} just solved {" and ".join(done.difference(puzzles_done[name]))}!', flush=True)
            puzzles_done[name] = done


