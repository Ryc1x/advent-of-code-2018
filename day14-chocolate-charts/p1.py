input = 864801

recipes = [3,7]
e1, e2 = 0,1
for i in range(900000):
    r1, r2 = recipes[e1], recipes[e2]
    l = [int(x) for x in str(r1+r2)]
    for x in l:
        recipes.append(x)
    e1 = (e1+r1+1) % len(recipes) 
    e2 = (e2+r2+1) % len(recipes)


print(*recipes[input:input+10],sep="")