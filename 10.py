import re

with open('10.input', 'r') as input_file:
    points = [tuple([int(n) for n in re.findall(('\-?\d+'), l)]) for l in input_file.readlines()]

def render(f):
    for y in range(min([p[1] for p in f]), max([p[1] for p in f]) + 1):
        line = ''
        for x in range(min([p[0] for p in f]), max([p[0] for p in f]) + 1):
            if (x, y) in f:
                line += '*'
            else:
                line += ' '
        print(line)
    return

frames = list()
frame_widths = list()

for i in range(100000):
    frame = [(p[0] + i * p[2], p[1] + i * p[3]) for p in points]
    frames.append(frame)
    frame_widths.append(max([p[0] for p in frame]) - min([p[0] for p in frame]))
    if frame_widths[i] > frame_widths[i-1]:
        render(frames[i-1])
        print(i -1)
        break