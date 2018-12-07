import re

f = open('input.txt', 'r')
input = f.readline()
f.close()
f = open('regex.txt', 'r')
regex = f.readline()
f.close()

l = len(input)
l2 = l+1
while (l != l2):
    l2 = l
    input = re.sub(regex,"",input)
    l = len(input)

# print(input) for part 2
print(l)