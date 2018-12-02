import string

import editdistance

with open('2.input', 'r') as input_file:
    ids = [l.strip() for l in input_file.readlines()]

# Part 1


def same_letters(id):
    char_counts = {char: id.count(char) for char in string.ascii_lowercase}
    return set(char_counts.values())


counts = {id: same_letters(id) for id in ids}

factors = {}

for f in [2, 3]:
    factors[f] = len([char_count for char_count in counts.values() if f in char_count])

checksum = factors[2] * factors[3]
print(checksum)


# Part 2

output = ''

for a in ids:
    for b in ids:
        if editdistance.eval(a, b) == 1:
            for pos, char in enumerate(a):
                if char == b[pos]:
                    output += char
            print(output)
