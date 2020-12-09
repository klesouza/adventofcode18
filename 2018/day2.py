import re

def part1(gen):
    count2 = 0
    count3 = 0
    for line in gen:
        counts = {
            1: [],
            2: [],
            3: [],
            4: []
        }
        for letter in line.replace('\n', ''):
            found=False
            for k,v in counts.items():
                if letter in v:
                    found = True    
                    if k != 4:
                        counts[k+1].append(letter)
                        counts[k].remove(letter)
                if found:
                    break
            if not found:    
                counts[1].append(letter)
        count2 += 1 if any(counts[2]) else 0
        count3 += 1 if any(counts[3]) else 0
    return count2*count3

def part2(gen):
    arr = list(gen)
    text = ''.join(arr)
    for linen in arr:
        line = linen.replace('\n','')
        for i in range(len(line)):
            rx = line[:i] + f"[^{line[i]}]" + line[i+1:]
            if re.compile(rx).search(text) is not None:
                return line[:i] + line[i+1:]