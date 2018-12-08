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
order = []

while len(ele) != 0:
    finish = min(d.keys(), key=lambda x: 1000*len(d[x])+ord(x))
    if (len(d[finish])) != 0:
        print('error')
    for e in d.keys():
        if finish in d[e]:
            d[e].remove(finish)
    del d[finish]
    order.append(finish)
    ele.remove(finish)

print("".join(order))