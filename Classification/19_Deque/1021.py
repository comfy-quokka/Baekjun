'''
start 20220304
end
'''

import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())
v = list(map(int, sys.stdin.readline().split()))
dq = deque(list(range(1,n+1)))
c = 0
for i in range(k):
    t = 0
    while True:
        tmp = dq.popleft()
        if tmp != v[i]:
            t += 1
            dq.append(tmp)
        else:
            if t > (n-i)/2:
                c += (n-i-t)
            else:
                c+=t
            break
print(c)