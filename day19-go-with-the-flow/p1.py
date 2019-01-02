# functions from day 16
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

reg = [1, 0, 0, 0, 0, 0]
il = []
ip = 0

f = open('input', 'r')
ipnum = int(f.readline()[4])
inputs = f.readlines()
f.close()

for s in inputs:
    l = s.split()
    ops = [int(x) for x in l[1:]]
    il.append([l[0]]+ops)

while ip in range(len(il)):
    reg[ipnum] = ip
    ans = [x for x in reg]
    i = il[ip]
    locals()[i[0]](i[1],i[2],i[3])
    ip = ans[ipnum]+1
    # if (ans[0] != reg[0]): print(reg)
    reg = ans

print(reg)


# PART 2:
# The program is calculating the sum of factors of reg[2],
# reg[2] is 10551430, so the answer is 18992592 (from factor.py)