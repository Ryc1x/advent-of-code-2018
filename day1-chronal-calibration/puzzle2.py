def puzzle2():
    f = open('input.txt', 'r')
    inputs = f.read().strip().split()
    f.close()
    x = 0
    results = set([0])
    while True:
        for a in inputs:
            x = x + int(a)
            if x in results:
                print(x)
                return
            results.add(x)

puzzle2()