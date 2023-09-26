#!/usr/bin/env python3
# Print lines when the puzzles in your private leaderboard were solved. Updates at most every 15 minutes since more is not allowed.
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
    # file with just the session id in it or session:"xx"
    COOKIE = f.read().strip().split(':')[-1].strip('"')

YEAR = sys.argv[1]
# TODO read from arg
LEADERBOARD_ID = 380357
STATS_URL = f'https://adventofcode.com/{YEAR}/leaderboard/private/view/{LEADERBOARD_ID}.json'
FILENAME = Path(dirname(abspath(__file__)) + f'/cache_{YEAR}.txt')

s = requests.session()


def get_from_cache() -> str:
    if not FILENAME.exists():
        return
    if datetime.fromtimestamp(FILENAME.stat().st_mtime) + timedelta(minutes=15) < datetime.now():
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


def get_stats():
    return get_from_cache() or update_cache()


if __name__ == '__main__':
    done_lines = []
    stats = json.loads(get_stats())
    for m in stats['members'].values():
        for day, parts in m['completion_day_level'].items():
            for part in parts:
                dt = datetime.fromtimestamp(m['completion_day_level'][day][part]['get_star_ts'])
                done_lines.append(f'[{dt.strftime("%Y-%m-%d %H:%M:%S")}] {m["name"]} solved {YEAR} day {day} part {part}!')
    print('\n'.join(sorted(done_lines)))
