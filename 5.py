import string

with open('5.input', 'r') as input_file:
    original = input_file.read()

search = [l + l.upper() for l in string.ascii_lowercase] + [l.upper() + l for l in string.ascii_lowercase]

def react(polymer):
    done = False

    while not done:
        start = len(polymer)
        for s in search:
            polymer = polymer.replace(s, '')
        done = (len(polymer) == start)

    return polymer

# Part 1

print(len(react(original)))

# Part 2

results = []

for l in string.ascii_lowercase:
    reduced = original.replace(l, '')
    reduced = reduced.replace(l.upper(), '')
    reduced = react(reduced)
    results.append(len(reduced))

print(min(results))