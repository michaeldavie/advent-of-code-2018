with open('2.input', 'r') as input_file:
    ids = [l.strip() for l in input_file.readlines()]

# Part 1

from itertools import product, combinations
from collections import Counter

factors = {2: 0,
           3: 0}

combos = product(ids, list(factors.keys()))

for id, f in combos:
    if f in set(Counter(id).values()):
        factors[f] += 1

print(factors[2] * factors[3])


# Part 2

import editdistance

for a, b in combinations(ids, 2):
    if editdistance.eval(a, b) == 1:
        print(''.join([char for pos, char in enumerate(a) if char == b[pos]]))
        break
