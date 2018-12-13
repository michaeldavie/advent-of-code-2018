import re

with open('12.input', 'r') as input_file:
    input_lines = input_file.readlines()

initial = re.search('[\.\#]+', input_lines[0]).group()
rules = {l[0:5]: l[9] for l in input_lines[2:]}

# Part 1

gen = list()
gen.append('..........' + initial + '.........................')

for i in range(1, 21):
    next_gen = '..'
    for p in range(2, len(gen[i-1])-2):
        next_gen += rules[gen[i-1][p-2:p+3]]
    next_gen += '..'
    gen.append(next_gen)

count = 0

for pos, char in enumerate(gen[20]):
    if char == '#':
        count += pos - 10

print(count)

# Part 2



pass