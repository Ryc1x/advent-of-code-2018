import re, string

f = open('part1.txt', 'r')
input = f.readline()
f.close()
f = open('regex.txt', 'r')
regex = f.readline()
f.close()

result = {}
for i in string.ascii_lowercase:
    remove = r'(?i)' + i
    improved = re.sub(remove,"",input)
    l = len(improved)
    l2 = l+1
    while (l != l2):
        l2 = l
        improved = re.sub(regex,"",improved)
        l = len(improved)
    result[i] = l

best = min(result.keys(), key=lambda x:result[x])

print(best,result[best])
