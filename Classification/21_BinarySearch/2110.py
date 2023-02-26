'''
start 20220311
end
'''

import sys

n, k = map(int, sys.stdin.readline().split())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
l.sort()
start = 0
end = l[-1]-l[0]
cp = l[0]

while True:
    mid = (start+end)//2
    c = [cp]
    for x in l:
        if x>=cp+mid:
            cp = x
            c.append(x)
    if start >= end and len(c) >= k:
        break
    elif len(c) >= k:
        start = mid+1
    else:
        end = mid-1
    cp = l[0]
print(mid)