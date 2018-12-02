def puzzle1():
    f = open('input.txt', 'r')
    inputs = f.read().strip().split()
    f.close()
    totalrep2 = 0
    totalrep3 = 0
    for s in inputs:
        # print(s)
        length = len(s)
        rep2 = False
        rep3 = False
        for c in s:
            repeats = 0
            for i in range(0, length):
                if (c == s[i]):
                    repeats += 1
            if (repeats == 2):
                rep2 = True
            if (repeats == 3):
                rep3 = True
        if (rep2):
            totalrep2 += 1
        if (rep3):
            totalrep3 += 1
        # print("TWO: ", totalrep2, "THREE: ", totalrep3)
    return totalrep2 * totalrep3

print(puzzle1())
        