from itertools import cycle

with open('9.input', 'r') as input_file:
    input_data = [(int(l.split()[0]), int(l.split()[6])) for l in input_file.readlines()]

players = input_data[0][0]
marble_count = input_data[0][1]
scores = [0 for p in range(players)]

marbles = list()
marbles.append(0)
current = 0
to_place = 1

for p in cycle(range(players)):
    if to_place > marble_count:
        break

    if (to_place) % 23 == 0:
        scores[p] += to_place + marbles[marbles.index(current)-7]
        del marbles[marbles.index(current)-7]
        current = marbles[marbles.index(current)-6]
        to_place += 1
        continue

    new_index = marbles.index(current) + 2
    if new_index > len(marbles):
        new_index = 1
    marbles.insert(new_index, to_place)
    current = to_place
    to_place += 1

print(max(scores))