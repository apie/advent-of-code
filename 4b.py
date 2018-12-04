#!/usr/bin/env python3
from operator import itemgetter
import datetime
import pytest

def get_guard_sleep_data(in_list_lines):
  asleep = dict()
  for l in in_list_lines:
    time_stamp=datetime.datetime.strptime(l.strip()[1:].split(']')[0], '%Y-%m-%d %H:%M')
    if '#' in l:
      guard_id=l.split('#')[1].split()[0]
    if 'falls asleep' in l:
      timer = time_stamp
    if 'wakes up' in l:
      duration = time_stamp - timer
      if guard_id not in asleep:
        asleep[guard_id] = dict(
          minutes_asleep=0,
          time_stamps=[]
        )
      asleep[guard_id]['minutes_asleep'] += (duration.seconds/60)
      asleep[guard_id]['time_stamps'].append((timer, time_stamp))

  return asleep

def sort_guards(d):
  return d[1][1]

def get_minute_sleep_frequencies(sleep_data):
  guards = dict()
  for guard_id, d in sleep_data.items():
    minutes = dict()
    for begin, end in d['time_stamps']:
      for m in range(1,60+1):
        if m>= begin.minute:
          if end.minute < begin.minute or end.minute > begin.minute and m<= end.minute:
            minutes[m] = minutes.get(m, 0) + 1
    guards[guard_id] = sorted(minutes.items(), reverse=True, key=itemgetter(1))[0]
  #dict guard_id, minute, freq
  return sorted(guards.items(), reverse=True, key=sort_guards)[0]

def answer(guard_id, minute):
  return int(guard_id) * minute

@pytest.fixture
def example_input():
  return '''
  [1518-11-01 00:00] Guard #10 begins shift
  [1518-11-01 00:05] falls asleep
  [1518-11-01 00:25] wakes up
  [1518-11-01 00:30] falls asleep
  [1518-11-01 00:55] wakes up
  [1518-11-01 23:58] Guard #99 begins shift
  [1518-11-02 00:40] falls asleep
  [1518-11-02 00:50] wakes up
  [1518-11-03 00:05] Guard #10 begins shift
  [1518-11-03 00:24] falls asleep
  [1518-11-03 00:29] wakes up
  [1518-11-04 00:02] Guard #99 begins shift
  [1518-11-04 00:36] falls asleep
  [1518-11-04 00:46] wakes up
  [1518-11-05 00:03] Guard #99 begins shift
  [1518-11-05 00:45] falls asleep
  [1518-11-05 00:55] wakes up
  '''

def test_most_asleep(example_input):
  sd = get_guard_sleep_data(example_input.strip().split('\n'))
  sf = get_minute_sleep_frequencies(sd)
  assert sf == ('99', (45, 3))
  assert answer(sf[0], sf[1][0]) == 4455


if __name__ == '__main__':
  with open('4.input', 'r') as in_list:
    sd = get_guard_sleep_data(sorted(in_list.readlines()))
    sf = get_minute_sleep_frequencies(sd)
    print(sf)
    ans = answer(sf[0], sf[1][0])
    print(ans)


