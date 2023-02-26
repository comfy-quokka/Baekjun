# 20220228

import sys
n = int(sys.stdin.readline())
ls = 0
t = []
for i in range(n):
    s, e = list(map(int, sys.stdin.readline().split()))
    ls = max(e+1,ls)
    t.append([s,e])
t.sort(key=lambda x:(x[0],x[1]))
c = 0
for i in range(n):
    s,e = t.pop()
    if ls >= e:
        c += 1
        ls = s
print(c)