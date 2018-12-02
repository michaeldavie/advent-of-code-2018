# Part 1

with open('1.input', 'r') as input_file:
    changes = [int(r) for r in input_file.readlines()]

output = 0

for c in changes:
    output += c

print('Part 1: ' + str(output))

# Part 2

output = 0
new_values = set()
found = None

while not found:
    for c in changes:
        output += c
        if output not in new_values:
            new_values.add(output)
        else:
            found = True
            print('Part 2: ' + str(output))
            break
