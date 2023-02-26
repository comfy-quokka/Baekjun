'''
start 20220304
end
'''

import sys
from collections import deque

n = int(sys.stdin.readline())
ans = []
for i in range(n):
    N, M = map(int,sys.stdin.readline().split())
    v = deque(list(map(int,sys.stdin.readline().split())))
    t = 0
    target = deque([0 for _ in range(N)])
    target[M] = 1
    while True:
        c = v.popleft()
        target_idx = target.popleft()
        if not v:
            t += 1
            break
        elif c >= max(v):
            if target_idx:
                t += 1
                break
            else:
                t+=1
        else:
            v.append(c)
            target.append(target_idx)
    ans.append(t)
for i in ans:
    print(i)