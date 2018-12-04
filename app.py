import re

def day1(gen):
    count = 0
    for line in gen:
        if '+' in line:
            count+= int(line[1:])
        elif '-' in line:
            count-= int(line[1:])
    return count

import sys
if __name__ == "__main__":
    day = sys.argv[1]
    with open(f'input{day}.txt', 'r') as f: 
        print(day1('+3, +3, +4, -2, -4'.split(', ')))
        # print(day1(f.readlines()))