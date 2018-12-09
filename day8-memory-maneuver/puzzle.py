# solution reference: Reddit@MichalMarsalek
def part1(l):
    child = l.pop(0)
    meta = l.pop(0)
    return sum(part1(l) for x in range(child)) + sum(l.pop(0) for x in range(meta))

def part2(l):
    child = l.pop(0)
    meta = l.pop(0)
    vals = [part2(l) for x in range(child)]
    metas = [l.pop(0) for x in range(meta)]
    if child == 0:
        return sum(metas)
    return sum(vals[i-1] for i in metas if i-1 in range(child))

def solve():
    f = open("input.txt", 'r')
    input = f.readline().split()
    f.close

    print(part1([int(x) for x in input]))
    print(part2([int(x) for x in input]))

solve()