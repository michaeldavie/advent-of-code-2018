from collections import Counter
from itertools import product
import re

import numpy
from scipy.spatial.distance import pdist, squareform

with open('6.test', 'r') as data_file:
    data = [tuple(map(int, re.findall('\d+', l))) for l in data_file.readlines()]

maxima = numpy.amax(data, 0)

layers = {}
keys = {}

for c in product(range(0, maxima[0] + 1), range(0, maxima[1] + 1)):
    layers[c] = numpy.ma.masked_equal(pdist(numpy.array([c] + data), 'cityblock'), 0, copy=False)

for l in layers:


    smallest = numpy.min(layers[c])
    if Counter(layers[c].flat)[smallest] == 1.0:
        keys[c] = numpy.argmin(layers[c])

counts = Counter(keys.values())

pass