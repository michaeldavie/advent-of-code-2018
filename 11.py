from itertools import product

input = 8199
grid = list(product(range(1, 301), range(1, 301)))

def power(cell):
    x = cell[0]
    y = cell[1]
    rack = x + 10
    p = rack * y
    p += input
    p = p * rack
    p = (p // 100) % 10
    p -= 5
    return p

power_cells = {cell: power(cell) for cell in grid}

totals = {}

#for (x, y) in product(range(1, 299), range(1, 299)):
#    totals[(x, y)] = sum([power_cells[(i, j)] for (i, j) in product(range(x, x + 3), range(y, y + 3))])

#print(max(totals, key=totals.get))

# Part 2

up_left = {}

for c in grid:
    up_left[c] = 0
    up_left += sum([power_cells[c] for c in grid if c[0] <= x and c[1] <= y])
    continue




    s = 2
    while x + s <= 301 and y + s <= 301:
        x2 = x + s - 1
        y2 = y + s - 1
        totals[(x, y, s)] = totals[(x, y, s - 1)] + sum([power_cells[(x2, i)] for i in range(y, y + s)]) + sum([power_cells[(j, y2)] for j in range(x, x2)])
        s += 1


for size in range(1, 301):
    for (x, y) in product(range(1, 300 - size - 1), range(1, 300 - size - 1)):
        totals[(x, y, size)] = sum([power_cells[(i, j)] for (i, j) in product(range(x, x + size), range(y, y + size))])

print(max(totals, key=totals.get))

pass
