def puzzle1():
    f = open('input.txt', 'r')
    inputs = f.readlines()
    f.close()

    # process inputs
    inputItems = []
    repeats = [False] * (len(inputs)+1)
    repeats[0] = True
    for s in inputs:
        inputItems.append(process(s))\

    w, h = 1000, 1000
    fabric = [[0 for x in range(w)] for y in range(h)] 
    for i in range(len(inputItems)):
        for j in range(inputItems[i][1],inputItems[i][1]+inputItems[i][3]):
            for k in range(inputItems[i][2],inputItems[i][2]+inputItems[i][4]):
                num = inputItems[i][0]
                if (fabric[j][k] == 0):
                    fabric[j][k] = num
                else:
                    repeats[fabric[j][k]] = True
                    repeats[num] = True
    
    return repeats.index(False)


def process(str):
    l = str.replace(" ","").split("#")[1].split("@")
    n = l[0]
    l = l[1].split(":")
    x = l[0].split(",")[0]
    y = l[0].split(",")[1]
    w = l[1].split("x")[0]
    h = l[1].split("x")[1]
    
    return [int(n), int(x), int(y), int(w), int(h)]

print(puzzle1())