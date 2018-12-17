def sum_metadata(arr, pos, total):
    if pos >= len(arr) or (total >0 and pos == 0):
        return pos, total
    i = pos
    n_nodes = arr[i]
    n_md = arr[i+1]
    if pos+2 < len(arr):
        i+=2
    
    while n_nodes > 0:
        i, total = sum_metadata(arr, i, total)
        n_nodes -= 1

    total += sum(arr[i:i+n_md])
    i += n_md
    return i, total

def part1(gen):
    input = list(map(lambda x: list(map(lambda y: int(y), x.split(' '))), gen))[0]
    return sum_metadata(input, 0, 0)

