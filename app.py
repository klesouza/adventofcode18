import re,itertools

def day1_2(gen):
    count = 0
    seen = {}
    for line in gen:
        if '+' in line:
            count+= int(line[1:])
        elif '-' in line:
            count-= int(line[1:])
        if count in seen:
            return count
        else:
            seen[count] = None
    return count

import sys
if __name__ == "__main__":
    day = sys.argv[1]
    def generator(p, n_iter=None):
        for i in (itertools.repeat(1, n_iter) if n_iter else itertools.repeat(1)):
            if type(p) == str:
                with open(p, 'r') as f:
                    for line in f.readlines():
                        yield line
            elif type(p) == list:
                for line in p:
                    yield line
    
    gen = generator(f'input{day}.txt')
    #gen = generator('+3, +3, +4, -2, -4'.split(', '))
    print(day1_2(gen))
        # print(day1(f.readlines()))