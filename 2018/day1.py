
def part2(gen):
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