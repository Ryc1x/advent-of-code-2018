f = open('input', 'r')
inputs = f.readlines()
f.close()

groups = [] # stores set of point index
points = [] # stores dict of points

for line in inputs:
    l = [int(x) for x in line.strip().split(',')]
    points.append({'a': l[0], 'b': l[1], 'c': l[2], 'd': l[3]})


def distance(p1, p2):
    d = 0
    for k in p1:
        d += abs(p1[k] - p2[k])
    return d

def addpoint(point):
    # if there are existing group, try to join one
    for g in groups:
        for p in g:
            if (distance(point,p) <= 3):
                points.remove(point)
                g.append(point)
                return True
    return False

while len(points) != 0:
    added = False
    for p in points:
        if addpoint(p): added = True
    if not added:
        groups.append([points[0]])
        points.pop(0)
    print(len(points))


print(len(groups))