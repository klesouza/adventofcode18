import re

def parse(line):
    return re.findall(r'\s([A-Z]{1})\s', line)
def init():
    return {
                'next': [],
                'prev': []
            }
def part1(gen):
    parsed = map(parse, gen)
    dag = {}
    next_iter = []
    for a,b in parsed:
        if a not in dag:
            dag[a] = init()
        if b not in dag:
            dag[b] = init()
        dag[a]['next'].append(b)
        dag[b]['prev'].append(a)
        if len(dag[a]['prev']) == 0 and a not in next_iter:
            next_iter.append(a)
        try:
            del next_iter[next_iter.index(b,0,len(next_iter))]
        except:
            pass
    final = []
    while next_iter:
        next_iter = sorted(next_iter)
        n = next_iter[0]
        if not dag[n].get('done', False) and all(map(lambda x: dag[x].get('done', False), dag[n]['prev'])):
            dag[n]['done'] = True
            final.append(n)
            next_iter.extend(dag[n]['next'])
        del next_iter[0]

    return ''.join(final)
    
