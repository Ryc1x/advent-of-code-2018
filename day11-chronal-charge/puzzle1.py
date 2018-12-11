sn = 2187
grid = [[0 for y in range(300)] for x in range(300)]

def pl(x,y):
    global sn
    rack = x + 10
    pl = rack * y + sn
    pl = pl * rack
    return int(str(pl)[-3]) - 5

def square(x,y):
    sum = 0
    for i in range(3):
        for j in range(3):
            sum += grid[x+i][y+j]
    return sum

for i in range(300):
    for j in range(300):
        grid[i][j] = pl(i,j)

best = 0
x = 0
y = 0
for i in range(297):
    for j in range(297):
        cur = square(i,j)
        if (cur > best):
            x, y = i, j
            best = cur

print(x,y)