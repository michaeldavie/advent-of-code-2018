with open('2.input', 'r') as input_file:
    ids = [l.strip() for l in input_file.readlines()]

# Part 1

from itertools import product, combinations
from collections import Counter

factors = Counter([match for id, match in product(ids, [2, 3]) if match in set(Counter(id).values())])

print(factors[2] * factors[3])


# Part 2

import editdistance

for a, b in combinations(ids, 2):
    if editdistance.eval(a, b) == 1:
        print(''.join([char for pos, char in enumerate(a) if char == b[pos]]))
        break
