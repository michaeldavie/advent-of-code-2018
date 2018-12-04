from collections import Counter
from itertools import chain, product
import re

with open('3.input', 'r') as input_file:
    claims = {int(num[0]): tuple([int(n) for n in num[1:5]]) for num in [re.findall('\d+', l) for l in input_file.readlines()]}

# Part 1

areas = {k: (range(t[0], t[0] + t[2]), range(t[1], t[1] + t[3])) for k, t in claims.items()}
unit_claims = Counter(chain.from_iterable([product(a[0], a[1]) for a in areas.values()]))
print(sum([v for k, v in Counter(unit_claims.values()).items() if k >= 2]))

# Part 2

single_claim = set([k for k, v in unit_claims.items() if v == 1])
area_sets = {k: set(product(a[0], a[1])) for k, a in areas.items()}
print([k for k, a in area_sets.items() if a.issubset(single_claim)])
