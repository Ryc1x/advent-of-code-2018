import math

f = open('input', 'r')
inputs = f.readlines()
f.close()

grid = []
carts = []

def show():
    copy = list(map(list,grid))
    for c in carts:
        copy[c['y']][c['x']] = '#'
    for r in copy:
        print(*r, sep="")

def play(ticks):
    for i in range(ticks):
        if (len(carts) == 1):
            return (carts[0]['x'],carts[0]['y'])
        copy = sorted(carts, key = lambda c: c['y']*1000+c['x'])
        for c in copy:
            rail = grid[c['y']][c['x']]
            if (rail == '+'):
                c['a'] += c['d']
                c['d'] = (c['d'])%3 -1
            elif (rail == '/'):
                c['a'] += 1 if c['a']%2==0 else -1
            elif (rail == '\\'):
                c['a'] += 1 if c['a']%2==1 else -1 
            c['x'] += int(math.cos(c['a']/2*math.pi))
            c['y'] += int(-math.sin(c['a']/2*math.pi))
            for c2 in carts:
                if (c['x'] == c2['x'] and c['y'] == c2['y'] and c != c2):
                    carts.remove(c)
                    carts.remove(c2)
                    # print("remove at x",c['x'],'y',c['y'])


for r in range(len(inputs)):
    s = inputs[r].strip('\n')
    for i in range(len(s)):
        c = s[i]
        if (c == '<'):
            carts.append({'x': i, 'y': r, 'a': 2,'d': 1})
        elif (c == '>'):
            carts.append({'x': i, 'y': r, 'a': 0,'d': 1})
        elif (c == '^'):
            carts.append({'x': i, 'y': r, 'a': 1,'d': 1})
        elif (c == 'v'):
            carts.append({'x': i, 'y': r, 'a': 3,'d': 1})
    l = list(s.replace('v','|').replace('^','|').replace('<','-').replace('>','-'))
    grid.append(l)

print(play(100000))