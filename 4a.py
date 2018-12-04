#!/usr/bin/env python3
from operator import itemgetter
import datetime
import pytest

def sort_sleep_dict(d):
  return d[1].get('minutes_asleep')

def get_guard_most_asleep(in_list_lines):
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

  return sorted(asleep.items(), reverse=True, key=sort_sleep_dict)[0]

def get_minute_most_asleep(stamps):
  minutes = dict()
  for begin, end in stamps:
    for m in range(1,60+1):
      if m>= begin.minute:
        if end.minute < begin.minute or end.minute > begin.minute and m<= end.minute:
          minutes[m] = minutes.get(m, 0) + 1
    
  return sorted(minutes.items(), reverse=True, key=itemgetter(1))[0][0]

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
  ma = get_guard_most_asleep(example_input.strip().split('\n'))
  assert ma[0] == '10'
  assert ma[1]['minutes_asleep'] == 50.0
  assert get_minute_most_asleep(ma[1]['time_stamps']) == 24
  assert answer('10', 24) == 240


if __name__ == '__main__':
  with open('4.input', 'r') as in_list:
    ma = get_guard_most_asleep(sorted(in_list.readlines()))
    print(ma[0])
    minute = get_minute_most_asleep(ma[1]['time_stamps'])
    print(minute)
    print(answer(ma[0], minute))


