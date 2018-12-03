with open('1.input', 'r') as input_file:
    changes = [int(r) for r in input_file.readlines()]

# Part 1

print(sum(changes))

# Part 2

from itertools import cycle

output = 0
new_values = set()

for c in cycle(changes):
    output += c
    if output not in new_values:
        new_values.add(output)
    else:
        print(str(output))
        break
