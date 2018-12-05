from collections import Counter
from datetime import datetime, timedelta
from itertools import chain, zip_longest
from operator import itemgetter
import re

with open('4.input', 'r') as data_file:
    lines = data_file.readlines()
lines.sort()

raw_logs = [(datetime.strptime(l[3:17], '%y-%m-%d %H:%M'), l[19:].strip()) for l in lines]
shifted_logs = [(l[0] + timedelta(hours=1), l[1]) for l in raw_logs]

# Part 1

guard_shifts = {l[0].date(): int(re.findall('#(\d+)', l[1])[0]) for l in shifted_logs if 'Guard' in l[1]}
nap_points = [(l[0].date(), l[0].minute,  l[1].split(' ')[0]) for l in shifted_logs if 'Guard' not in l[1]]

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

nap_stats = [(n[0][0], range(n[0][1], n[1][1]), n[1][1] - n[0][1]) for n in grouper(nap_points, 2)]
naps = [{'date': n[0], 'guard': guard_shifts[n[0]], 'span': n[1], 'duration': n[2]} for n in nap_stats]
guard_totals = {g: sum([n['duration'] for n in naps if n['guard'] == g]) for g in set(guard_shifts.values())}
sleepy_guard = max(guard_totals.items(), key=itemgetter(1))[0]

sleepy_minutes = Counter(chain.from_iterable([n['span'] for n in naps if n['guard'] == sleepy_guard]))
sleepiest_minute = max(sleepy_minutes.items(), key=itemgetter(1))[0]
print(sleepy_guard * sleepiest_minute)

# Part 2

sleepy_minutes_all = {g: Counter(chain.from_iterable([n['span'] for n in naps if n['guard'] == g])) for g in guard_shifts.values()}
tuple_madness = [(g, v.most_common(1)[0][0], v.most_common(1)[0][1]) for g, v in sleepy_minutes_all.items() if v]
tip_top = max(tuple_madness, key=itemgetter(2))
print(tip_top[0] * tip_top[1])