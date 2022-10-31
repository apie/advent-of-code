#!/usr/bin/env python3
# Print a line when someone from your private leaderboard on adventofcode.com solves a puzzle. Updates at most every 15 minutes since more is not allowed.
# By Apie 2021-12-13

import sys
import os
import requests
#from requests.exceptions import JSONDecodeError
import json
from datetime import datetime, timedelta
from pathlib import Path
from os.path import dirname, abspath
from time import sleep


COOKIE_FILE = dirname(abspath(__file__)) + '/../cookie.txt'
with open(COOKIE_FILE) as f:
    COOKIE = f.read().strip()

YEAR = sys.argv[1]
UPDATE_FREQ_MINUTES = 1 if len(sys.argv) == 2 else int(sys.argv[2])
LEADERBOARD_ID = 380357
STATS_URL = f'https://adventofcode.com/{YEAR}/leaderboard/private/view/{LEADERBOARD_ID}.json'
FILENAME = Path(dirname(abspath(__file__)) + f'/cache_{YEAR}.txt')

s = requests.session()


def get_from_cache(remove_old_cache=True) -> str:
    if not FILENAME.exists():
        return
    if remove_old_cache and datetime.fromtimestamp(FILENAME.stat().st_mtime) + timedelta(minutes=15) < datetime.now():
        os.remove(FILENAME)
        return
    with open(FILENAME) as f:
        return f.read()


def update_cache():
    r = s.get(STATS_URL, cookies=dict(session=COOKIE), timeout=5)
    r.raise_for_status()
    stats = r.text
    try:
        r.json()
    except:
        raise Exception('Response was not JSON. You probably need to renew your cookie!')
    with open(FILENAME, "w") as f:
        f.write(stats)
    return stats


def get_stats(remove_old_cache=True):
    return get_from_cache(remove_old_cache) or update_cache()


def get_done_set(m):
    return {
        'day ' + day + ' part ' + part
        for day, parts in m['completion_day_level'].items()
        for part in parts
    }


if __name__ == '__main__':
    puzzles_done = dict()
    # Keep old cache so that we get notified of all the differences since the last time.
    stats = json.loads(get_stats(remove_old_cache=False))
    for m_id, m in stats['members'].items():
        name = m['name']
        puzzles_done[name] = get_done_set(m)

    while True:
        sleep(60 * UPDATE_FREQ_MINUTES)
        stats = json.loads(get_stats())
        for m_id, m in stats['members'].items():
            done = get_done_set(m)
            name = m['name']
            if len(done) == len(puzzles_done[name]):
                continue  # nothing changed
            for p_done in sorted(done.difference(puzzles_done[name])):
                _, day, _, part = p_done.split()
                dt = datetime.fromtimestamp(m['completion_day_level'][day][part]['get_star_ts'])
                print(f'[{dt.strftime("%Y-%m-%d %H:%M:%S")}] {name} solved {YEAR} {p_done}!', flush=True)
            # Save new state
            puzzles_done[name] = done
