from collections import deque

with open('8.input', 'r') as input_file:
    input_deque = deque(int(n) for n in input_file.read().split())

# Part 1

def sum_meta(data_deque):
    children = data_deque.popleft()
    metas = data_deque.popleft()
    meta_sum = 0

    for c in range(children):
        meta_sum += sum_meta(data_deque)

    meta_sum += sum([data_deque.popleft() for m in range(metas)])

    return meta_sum

print(sum_meta(input_deque.copy()))

# Part 2

def node_value(data_deque):
    children = data_deque.popleft()
    meta_count = data_deque.popleft()

    value = 0
    child_values = []

    if children > 0:
        for c in range(children):
            child_values.append(node_value(data_deque))

    meta_values = [data_deque.popleft() for m in range(meta_count)]

    if children == 0:
        return sum(meta_values)

    for m in meta_values:
        if m == 0 or m > children:
            continue
        value += child_values[m - 1]

    return value

print(node_value(input_deque.copy()))