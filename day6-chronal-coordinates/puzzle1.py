w, h = 400, 400
grid = [[0 for x in range(w)] for y in range(h)]

def puzzle1():
    f = open('input.txt', 'r')
    input = f.readlines()
    f.close()

    coord = {}
    for i in range(len(input)):
        c = input[i].split(",")
        coord[i] = ([int(c[0]),int(c[1])])

    for i in range(w):
        for j in range(h):
            l = []
            for k, v in coord.items():
                l.append([k,abs(i-v[0])+abs(j-v[1])])
            l.sort(key=lambda x: x[1])
            grid[i][j] = -1 if l[0][1] == l[1][1] else l[0][0]

    d = {}
    for i in range(w):
        for j in range(h):
            if (i==0 or j == 0 or i == (w-1) or j == (h-1)):
                d[grid[i][j]] = -100000
            d[grid[i][j]] = d[grid[i][j]]+1 if grid[i][j] in d else 1


    print(sorted(d.items(), key=lambda kv: kv[1]))

    # show()


def show():
    f = open("out.txt", "w")
    for r in grid:
        f.write(" ".join(str(x) for x in r))
        f.write("\n")
    f.close()
            
puzzle1()