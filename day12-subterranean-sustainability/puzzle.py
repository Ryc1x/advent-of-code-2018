pots = "..##.#######...##.###...#..#.#.#..#.##.#.##....####..........#..#.######..####.#.#..###.##..##..#..#"

f = open('input', 'r')
inputs = f.readlines()
f.close

rules = {}
for s in inputs:
    l = s.split()
    rules[l[0]] = l[2]

pots = ".............................." + pots + ".............................."
for i in range(20):
    next = ["." for x in range(len(pots))]
    for i in range(len(pots)-5):
        config = pots[i:i+5]
        next[i+2] = rules[config]
    pots = "".join(next)
    print(pots)

sum = 0
for i in range(len(pots)):
    if (pots[i] == "#"):
        sum += (i-30)

print(sum)