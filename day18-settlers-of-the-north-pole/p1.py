# This file includes both parts

def surround(x,y):
    d = {'.': 0, '|': 0, '#': 0}
    d[grid[y-1][x-1]] += 1
    d[grid[y-1][x]  ] += 1
    d[grid[y-1][x+1]] += 1
    d[grid[y]  [x-1]] += 1
    d[grid[y]  [x+1]] += 1
    d[grid[y+1][x-1]] += 1
    d[grid[y+1][x]  ] += 1
    d[grid[y+1][x+1]] += 1
    return d
    
f = open('input', 'r')
inputs = f.readlines()
f.close()

w, h = len(inputs[0].strip()), len(inputs)
grid = []

# add an additional layer of open ground
grid.append(['.' for x in range(w+2)])
for s in inputs:
    grid.append(['.']+list(s.strip())+['.'])
grid.append(['.' for x in range(w+2)])

for i in range(11):
    # Show grid
    # print(i, "minutes")
    # for r in grid:
    #     print(*r,sep="")
    # print()
    t, l = 0, 0
    copy = [r[:] for r in grid]
    for y in range(1,w+1):
        for x in range(1,h+1):
            a = grid[y][x]
            if a == '.':
                if surround(x,y)['|'] >= 3:
                    copy[y][x] = '|'
            elif a == '|':
                t += 1
                if surround(x,y)['#'] >= 3:
                    copy[y][x] = '#'
            elif a == '#':
                l += 1
                if surround(x,y)['|'] < 1 or surround(x,y)['#'] < 1:
                    copy[y][x] = '.'
    grid = [r[:] for r in copy]
    print("After", i , "m:", t*l)

# PART TWO
# starts after 1000 minutes, score = 165376, repeat every 28 minutes
# (1000000000-1000)/28 = 35714250 (no remainder) ->  ANSWER: 165376