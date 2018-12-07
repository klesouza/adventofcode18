import itertools
import numpy as np

def distance(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)
def sorted_by(it, idx):
    return sorted(
        it,
        key = lambda coord: coord['arr'][idx])

def part1(gen):
    ns = itertools.count(0,1)
    x_sorted = sorted_by(
        map(lambda pos: {'id': ns.__next__(), 'dist': 0,'arr': [int(x.strip()) for x in pos.split(',')]}, gen),
        0)
    y_sorted = sorted_by(x_sorted, 1)

    minx = x_sorted[0]['arr'][0]
    maxx = x_sorted[-1]['arr'][0]
    miny = y_sorted[0]['arr'][1]
    maxy = y_sorted[-1]['arr'][1]
    infinte = []
    for x in range(minx, maxx+1):
        for y in range(miny, maxy+1):
            m = sorted(x_sorted,
                key=lambda item: distance(item['arr'][0], item['arr'][1], x, y))
            
            if distance(m[0]['arr'][0], m[0]['arr'][1], x, y) == distance(m[1]['arr'][0], m[1]['arr'][1], x, y):
                continue
            
            if x in [minx, maxx] or y in [maxy, miny]:
                infinte.append(m[0]['id'])
            # if distance(m[0]['arr'][0], m[0]['arr'][1], x, y) > 0:
            m[0]['dist'] += 1
    # print(x_sorted)
    return max(filter(lambda x: x['id'] not in infinte, x_sorted), key=lambda item: item['dist'])
        