# define functions
def addr(a, b, c): ans[c] = reg[a] + reg[b]
def addi(a, b, c): ans[c] = reg[a] + b
def mulr(a, b, c): ans[c] = reg[a] * reg[b]
def muli(a, b, c): ans[c] = reg[a] * b
def banr(a, b, c): ans[c] = reg[a] & reg[b]
def bani(a, b, c): ans[c] = reg[a] & b
def borr(a, b, c): ans[c] = reg[a] | reg[b]
def bori(a, b, c): ans[c] = reg[a] | b
def setr(a, b, c): ans[c] = reg[a]
def seti(a, b, c): ans[c] = a
def gtir(a, b, c): ans[c] = 1 if a > reg[b] else 0
def gtri(a, b, c): ans[c] = 1 if reg[a] > b else 0
def gtrr(a, b, c): ans[c] = 1 if reg[a] > reg[b] else 0
def eqir(a, b, c): ans[c] = 1 if a == reg[b] else 0
def eqri(a, b, c): ans[c] = 1 if reg[a] == b else 0
def eqrr(a, b, c): ans[c] = 1 if reg[a] == reg[b] else 0

reg = [0,0,0,0]
fl = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
a,b,o = [], [], []

f = open('input1', 'r')
inputs = f.readlines()
f.close()

for s in inputs:
    if s[0] == 'B':
        b.append([int(s[9]), int(s[12]), int(s[15]), int(s[18])])
    elif s[0] == 'A':
        a.append([int(s[9]), int(s[12]), int(s[15]), int(s[18])])
    elif s[0] != '\n':
        o.append([int(x) for x in s.split()])

count = 0
for i in range(len(a)):
    reg = b[i]
    ans = [x for x in reg]
    ops = 0
    for f in fl:
        f(o[i][1], o[i][2], o[i][3])
        if (ans == a[i]): 
            ops += 1
    if (ops >= 3):
        count += 1

print(count)
