from itertools import cycle
import time

with open('9.input', 'r') as input_file:
    input_data = [(int(l.split()[0]), int(l.split()[6])) for l in input_file.readlines()]

start = time.time()

players = input_data[0][0]
marble_count = input_data[0][1]
scores = [0 for p in range(players)]

marbles = list()
marbles.append(0)
current_pos = 0
to_place = 1

for p in cycle(range(players)):
    if to_place > marble_count:
        break

    if to_place % 23 == 0:
        scores[p] += to_place + marbles[current_pos-7]
        del marbles[current_pos-7]
        current_pos = current_pos-7
        if current_pos < 0:
            current_pos += len(marbles) + 1
        to_place += 1
        continue

    new_index = current_pos + 2
    if new_index > len(marbles):
        new_index = 1
    marbles.insert(new_index, to_place)
    current_pos = new_index
    to_place += 1

print(max(scores))

print("------- {:.3f} seconds -------".format(time.time() - start))
