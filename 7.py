from collections import defaultdict
import re

with open('7.test', 'r') as input_file:
    input_lines = input_file.readlines()

def parse_rules():
    rules_list = [re.findall(' ([A-Z])', l) for l in input_lines]
    rules_dict = defaultdict(list)

    for first, second in rules_list:
        rules_dict[second].append(first)
        if first not in rules_dict:
            rules_dict[first] = []

    return rules_dict

# Part 1

rules_dict = parse_rules()
passed = []

while not all([v == [] for v in rules_dict.values()]):
    current_step = sorted(set([k for k, v in rules_dict.items() if v == []]) - set(passed))[0]
    passed.append(current_step)
    for v in rules_dict.values():
        if current_step in v:
            v.remove(current_step)

passed.append((set(rules_dict.keys()) - set(passed)).pop())

print(''.join(passed))

# Part 2

rules_dict = parse_rules()
passed = []
worker_tasks = {n: '' for n in range(0, 2)}

while not all([v == [] for v in rules_dict.values()]):
    open_steps = sorted(set([k for k, v in rules_dict.items() if v == []]) - set(passed))


pass