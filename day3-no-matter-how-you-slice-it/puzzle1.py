def puzzle1():
    f = open('input.txt', 'r')
    inputs = f.readlines()
    f.close()

    # process inputs
    inputItems = []
    for s in inputs:
        inputItems.append(process(s))

    w, h = 1000, 1000
    fabric = [[0 for x in range(w)] for y in range(h)] 
    for i in range(len(inputItems)):
        for j in range(inputItems[i][1],inputItems[i][1]+inputItems[i][3]):
            for k in range(inputItems[i][2],inputItems[i][2]+inputItems[i][4]):
                fabric[j][k] += 1

    count = 0
    for i in range(w):
        for j in range(h):
            if (fabric[i][j] >= 2):
                count += 1
    
    return count

# better use regex XD 
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
        