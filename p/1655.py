'''
start 20220315
end
'''

import sys
import heapq

n = int(sys.stdin.readline())
q1 = []
q2 = []
ans = []

for i in range(n):
    a = int(sys.stdin.readline())
    if not q1:
        heapq.heappush(q1,-a)
        ans.append(a)
    elif i%2 == 1:
        if -q1[0] < a:
            heapq.heappush(q2, a)
            ans.append(-q1[0])
        else:
            heapq.heappush(q2,-heapq.heappop(q1))
            heapq.heappush(q1, -a)
            ans.append(-q1[0])
    else:
        if -q1[0] > a:
            heapq.heappush(q1, -a)
            ans.append(-q1[0])
        else:
            heapq.heappush(q2, a)
            heapq.heappush(q1, -heapq.heappop(q2))
            ans.append(-q1[0])
for i in range(n):
    print(ans[i])