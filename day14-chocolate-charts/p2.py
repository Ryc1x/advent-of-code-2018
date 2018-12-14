input = 864801

# Coped first 15 recipes for indexing later
recipes = [3, 7, 1, 0, 1, 0, 1, 2, 4, 5, 1, 5, 8, 9, 1, 6, 7, 7, 9, 2]
e1, e2 = 8,4
for i in range(100000000):
    r1, r2 = recipes[e1], recipes[e2]
    l = [int(x) for x in str(r1+r2)]
    for x in l:
        recipes.append(x)
    e1 = (e1+r1+1) % len(recipes) 
    e2 = (e2+r2+1) % len(recipes)
    if (100000*recipes[i]+10000*recipes[i+1]+1000*recipes[i+2]+100*recipes[i+3]+10*recipes[i+4]+recipes[i+5] == input):
        print(i)
