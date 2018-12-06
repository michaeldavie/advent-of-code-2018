import string

with open('5.input', 'r') as input_file:
    original = input_file.read()

# Part 1

search = [l + l.upper() for l in string.ascii_lowercase] + [l.upper() + l for l in string.ascii_lowercase]

def react(polymer):
    done = False

    while not done:
        start = len(polymer)
        for s in search:
            polymer = polymer.replace(s, '')
        done = True if len(polymer) == start else False

    return polymer

reacted = react(original)
print(len(reacted))

# Part 2

results = []

for l in search:
    reduced = original.replace(l[0], '')
    reduced = reduced.replace(l[1], '')
    reduced = react(reduced)
    results.append(len(reduced))

print(min(results))