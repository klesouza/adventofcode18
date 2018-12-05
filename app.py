import re,itertools
from . import *

import sys
def generator(p, n_iter=None):
    for i in (itertools.repeat(1, n_iter) if n_iter else itertools.repeat(1)):
        if type(p) == str:
            with open(p, 'r') as f:
                for line in f.readlines():
                    yield line
        elif type(p) == list:
            for line in p:
                yield line
if __name__ == "__main__":
    day = sys.argv[1]
    part = sys.argv[2] if len(sys.argv) > 2 else '1'
    test = 'test' if len(sys.argv) > 3 else ''
    gen = generator(f'input{day}{test}.txt', 1)
    print(getattr(__import__(f"day{day}"), f'part{part}')(gen))
    
        # print(day1(f.readlines()))