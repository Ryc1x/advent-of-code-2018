w, h = 400, 400
grid = [[0 for x in range(w)] for y in range(h)]

def puzzle2():
    f = open('input.txt', 'r')
    input = f.readlines()
    f.close()

    coord = {}
    for i in range(len(input)):
        c = input[i].split(",")
        coord[i] = ([int(c[0]),int(c[1])])

    count = 0
    for i in range(w):
        for j in range(h):
            l = []
            for v in coord.values():
                l.append(abs(i-v[0])+abs(j-v[1]))
            count += 1 if sum(l) < 10000 else 0

    print(count)

puzzle2()