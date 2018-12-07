import collections

# Referenced reddit @vash3r's solution
def puzzle1():
    f = open('sorted.txt', 'r')
    inputs = f.readlines()
    f.close()

    guards = collections.defaultdict(lambda:[0 for x in range(60)])

    for s in inputs:
        if s[25]=="#": # new guard
            g=s.split()[3]
        elif s[25]=="a": # falls asleep
            st=int(s[15:17])
        else: # wake up
            t=int(s[15:17])
            for x in range(st,t):
                guards[g][x]+=1
    # part 1 - guard who sleep most
    g1 = min(guards.keys(), key=lambda g:-sum(guards[g]))
    # part 2 - guard who sleep most at same minute
    g2 = min(guards.keys(), key=lambda g:-max(guards[g]))
    print(sorted(guards.keys(), key=lambda g:-max(guards[g])))

    for g in [g1,g2]:
        gh = guards[g]
        minute = gh.index(max(gh))
        print(int(g[1:])*minute)
    
#     # process inputs
#     items = []
#     for s in inputs:
#         items.append(s.split())
    
#     guards = {0: [0]}
#     minutes = {}
#     num = 0
#     for i in items:
#         if (i[2] == 'g'):
#             if (num in minutes):
#                 minutes[num] += calc(guards[num])
#             else:
#                 minutes[num] = calc(guards[num])
#             num = i[3]
#             guards[num] = [minute(i[1])]
#             print(guards[num])
#         else:
#             guards[num].append(minute(i[1]))

#     del minutes[0]

#     id = min(minutes, key=minutes.get)
#     time = minutes[id]

#     print(minutes)

#     print("ID: ", id)
#     print("Time: ", time)

# def minute(time):
#     hour = time.split(":")[0]
#     minute = time.split(":")[1]

#     return int(minute) + (0 if (int(hour) < 1) else -60)

# def calc(list):
#     time = 0
#     if (list[0] < 0):
#         list[0] = 0
    
#     for i in range(1,len(list),2):
#         time += (int(list[i])-int(list[i-1]))
    
#     return time + (60-list[-1])




puzzle1()
        