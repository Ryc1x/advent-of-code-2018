def puzzle1():
    f = open("input.txt","r")
    x = 0
    for a in f:
        x = x + int(a)
    print(x)

puzzle1()