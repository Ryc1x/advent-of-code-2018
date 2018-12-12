pots = "..##.#######...##.###...#..#.#.#..#.##.#.##....####..........#..#.######..####.#.#..###.##..##..#..#"

def sum():
    sum = 0
    for i in range(len(pots)):
        if (pots[i] == "#"):
            sum += (i+start)
    return sum

f = open('input', 'r')
inputs = f.readlines()
f.close

rules = {}
for s in inputs:
    l = s.split()
    rules[l[0]] = l[2]

pots = ".........." + pots + ".........."
start = -10
for c in range(50000000000):
    next = ["." for x in range(len(pots))]
    for i in range(len(pots)-5):
        config = pots[i:i+5]
        next[i+2] = rules[config]
    pots = "".join(next)
    if (pots[:5] != "....."):
        pots = "....." + pots
        start -= 5
    elif (pots[:10] == ".........."):
        pots = pots[5:]
        start += 5
    if (pots[-5:] != "....."):
        pots = pots + "....."
    elif (pots[-10:] == ".........."):
        pots = pots[:-5]
    if (c%10000 == 9999):
        print(c)
        print(sum())

# pattern: start from iteration#9999 = 510883 | +510000 per 10000 interation (or 51 per iteration)
# ans: 51*50,000,000,000 + 883 = 2550000000883