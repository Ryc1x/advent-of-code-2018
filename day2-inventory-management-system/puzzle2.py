# for this one I mannually compare the strings that off by one XD

def puzzle2():
    f = open('input.txt', 'r')
    inputs = f.read().strip().split()
    f.close()
    for s1 in inputs:
        # print(s1)
        length = len(s1)
        for s2 in inputs:
            diffs = 0
            for i in range(0, length):
                if (s1[i] != s2[i]):
                    diffs += 1
            if (diffs == 1):
                print ("S1: ", s1, "S2: ", s2)
                return
    return

puzzle2()