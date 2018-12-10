# I got part two first then part one XDD

f = open('input', 'r')
inputs = f.readlines()
f.close()

stars = {}

def msg():
    lx = sorted(stars.values(), key=lambda s: s['x'])
    ly = sorted(stars.values(), key=lambda s: s['y'])
    xmin, xmax = lx[0]['x'], lx[-1]['x']
    ymin, ymax = ly[0]['y'], ly[-1]['y']
    sky = [['.' for x in range(xmax-xmin+1)] for y in range(ymax-ymin+1)]
    for s in stars:
        sky[stars[s]['y']-ymin][stars[s]['x']-xmin] = '#'
    for r in sky:
        print(*r, sep=" ")
    print()

for i in range(len(inputs)):
    cor = inputs[i].split('>')[0].split('<')[1]
    vel = inputs[i].split('>')[1].split('<')[1]
    x = int(cor.split(',')[0])
    y = int(cor.split(',')[1])
    dx = int(vel.split(',')[0])
    dy = int(vel.split(',')[1])
    stars[i] = {'x': x, 'y': y, 'dx': dx, 'dy': dy}

move = 0
size = 1000000
for i in range(10577):
    for s in stars:
        stars[s]['x'] += stars[s]['dx']
        stars[s]['y'] += stars[s]['dy']
    
    # PART TWO
    lx = sorted(stars.values(), key=lambda s: s['x'])
    xmin, xmax = lx[0]['x'], lx[-1]['x']
    if (xmax-xmin < size):
        size = xmax-xmin
        move = i+1 # move=10577

# PART ONE
print('At', move, 's')
msg()