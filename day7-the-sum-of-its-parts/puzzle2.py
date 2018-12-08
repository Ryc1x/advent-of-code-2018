f = open('input.txt','r')
input = f.readlines()
f.close()

l = []
d = {}
for s in input:
    ls = s.split()
    s1, s2 = ls[1], ls[7]
    l.append([s1,s2])
    if s1 not in d:
        d[s1] = []
    if s2 not in d:
        d[s2] = []


for i in l:
    i1, i2 = i[0], i[1]
    d[i2].append(i1)

ele = set(d.keys())
time = 0
workers = [[-1,''],[-1,''],[-1,''],[-1,''],[-1,'']]

while len(ele) != 0:
    filtered = {k: v for k, v in d.items() if len(v) == 0}
    finish = sorted(filtered.keys(), key=lambda x: ord(x))
    n = 0
    for w in range(5):
        if (workers[w][0] <= 0):
            # do work if there is one
            if (n < len(finish)):
                workers[w][1] = finish[n]
                del d[finish[n]]
                workers[w][0] = ord(finish[n]) - 5
                n += 1
        # finish work
        if (workers[w][0] == 0):
            for e in d.keys():
                if workers[w][1] in d[e]:
                    d[e].remove(workers[w][1])
            ele.remove(workers[w][1])
        workers[w][0] -= 1
    time += 1

print(time)