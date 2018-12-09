# Idea from Reddit@MichalMarsalek 
# Use deque instead of list for much better performance (and looks better XD)

from collections import deque

players = 471
last = 7202600

elves = {k:v for k, v in [(x,0) for x in range(1,players+1)]}
marbles = deque([0])

e = 0

for m in range(1,last+1):
    e = 1 if e >= players else e+1
    if (m%23 == 0):
        marbles.rotate(-7)
        elves[e] += (m + marbles.pop())
    else:
        marbles.rotate(2)
        marbles.append(m)

print(max(elves.values()))