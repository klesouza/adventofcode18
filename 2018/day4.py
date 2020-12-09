import re

g_id = lambda x: re.search(r'#([0-9]+)', x).groups()[0]
minute = lambda x: x[15:17]

def parse_line(x):
    return {
        'time': x[1:17],
        'minute': int(minute(x)),
        'id': g_id(x) if 'Guard' in x else None
    }

def compute_guards(gen):
    s = sorted(map(parse_line, gen), key=lambda x: x['time'])
    guards = {}
    i = 0
    current_guard = None
    while i < len(s):
        line = s[i]
        if line['id'] is not None:
            i += 1
            current_guard = line['id']
            if line['id'] not in guards:
                guards[line['id']] = {
                    'max': -1,
                    'mins': [0 for _ in range(60)],
                    'sum': 0
                    }
            continue

        start = s[i]['minute']
        end = s[i+1]['minute']
        for j in range(start,end):
            guards[current_guard]['mins'][j] += 1
            guards[current_guard]['sum'] += 1
            if guards[current_guard]['mins'][j] > guards[current_guard]['mins'][guards[current_guard]['max']]:
                guards[current_guard]['max'] = j
        i += 2
    return guards
def part1(gen):
    guards = compute_guards(gen)
    # for k,v in guards.items():
    #     s = sum(v['mins'])
    #     print(f'{k} - {s}')
    g = sorted(guards, key=lambda x: guards[x]['sum'], reverse=True)[0]
    
    return int(g)*guards[g]['max']

def part2(gen):
    guards = compute_guards(gen)
    g = sorted(guards, key=lambda x: guards[x]['mins'][guards[x]['max']], reverse=True)[0]
    print(g)
    return int(g)*guards[g]['max']