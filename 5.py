from collections import deque
import string
import time

with open('5.input', 'r') as input_file:
    original = input_file.read()

start = time.time()

def react(polymer):
    in_deque = deque(polymer)
    out_deque = deque()
    buffer = in_deque.popleft()

    while in_deque:
        if buffer != in_deque[0] and buffer.lower() == in_deque[0].lower():
            in_deque.popleft()
            buffer = out_deque.pop() if out_deque else in_deque.popleft()
        else:
            out_deque.append(buffer)
            buffer = in_deque.popleft()

    return ''.join(out_deque) + buffer

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

print("------- {:.3f} seconds -------".format(time.time() - start))
