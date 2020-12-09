import re, gc
def part1(gen):
    text = list(gen)[0]
    i = 1
    while i < len(text):
        if i > 0 and abs(ord(text[i]) - ord(text[i-1])) == 32:
            text = text[0:i-1]+text[i+1:]
            i -= 1
        else:
            i += 1
    return len(text)

def part2(gen):
    text_or = list(gen)[0]
    m = None
    min_l = None
    for l in [chr(x) for x in range(97, 123)]:
        if re.search(l, text_or, re.I) is None:
            continue
        text = text_or.replace(l, '').replace(l.upper(), '')
        i = 0
        while i < len(text):
            if i > 0 and abs(ord(text[i]) - ord(text[i-1])) == 32:
                text = text[0:i-1]+text[i+1:]
                i -= 1
            else:
                i += 1
        if m is None or m > len(text):
            m = len(text)
            min_l = l
    print(min_l)
    return m