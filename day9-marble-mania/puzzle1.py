# This one uses list which has bad performance, which cannot solve part2 

players = 471
last = 72026

elves = {k:v for k, v in [(x,0) for x in range(1,players+1)]}
marbles = [0]

c = 0
e = 0

for m in range(1,last+1):
    e = 1 if e >= players else e+1
    if (m%23 == 0):
        c = c-7 if c > 7 else len(marbles)+c-7
        elves[e] += (m + marbles.pop(c))
    else:
        c = (c+2) % len(marbles) if (c+2) % len(marbles) != 0 else len(marbles)
        marbles.insert(c, m)

print(max(elves.values()))