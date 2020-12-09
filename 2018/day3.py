import re

def print_matrix(m):
    print('\n'.join([str(x) for x in m]))

def part1(gen):
    fabric = [[0 for _ in range(1000)] for _ in range(1000)]
    count = 0
    for line in gen:
        rx = r'(\d+)[^\d]+(\d+),(\d+)[^\d]+(\d+)x(\d+)'
        id,in_left, in_top, w, h = map(lambda x: int(x), re.search(rx, line).groups())
        for i in range(in_top, in_top+h):
            for j in range(in_left, in_left+w):
                fabric[i][j] += 1
                if fabric[i][j] == 2:
                    count += 1
    return count

def part2(gen):
    fabric = [[None for _ in range(1000)] for _ in range(1000)]
    count = 0
    ids = []
    for line in gen:
        rx = r'(\d+)[^\d]+(\d+),(\d+)[^\d]+(\d+)x(\d+)'
        id,in_left, in_top, w, h = map(lambda x: int(x), re.search(rx, line).groups())
        ids.append(id)
        for i in range(in_top, in_top+h):
            for j in range(in_left, in_left+w):
                if fabric[i][j] is None:
                    fabric[i][j] = id
                else:
                    if id in ids:
                        ids.remove(id)
                    if fabric[i][j] in ids:
                        ids.remove(fabric[i][j])
    return ids  