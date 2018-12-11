sn = 2187
grid = [[0 for y in range(300)] for x in range(300)]

def pl(x,y):
    global sn
    rack = x + 10
    pl = rack * y + sn
    pl = pl * rack
    return int(str(pl)[-3]) - 5

def square(x,y,size):
    sum = 0
    for i in range(size):
        for j in range(size):
            sum += grid[x+i][y+j]
    return sum

for i in range(300):
    for j in range(300):
        grid[i][j] = pl(i,j)

best = 0
x = 0
y = 0
size = 0
# I tried to print out the largest result for each size and it stop growing after 13
for i in range(1,15):
    # print("size",i)
    for j in range(300-i):
        for k in range(300-i):
            cur = square(j,k,i)
            if (cur > best):
                x, y = j,k
                best = cur
                size = i
    # print("max: ", best)

print(x,y,size)