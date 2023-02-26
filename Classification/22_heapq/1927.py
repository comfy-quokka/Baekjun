'''
start 20220315
end
'''

import heapq
import sys

heap = []

n = int(sys.stdin.readline())

for i in range(n):
    a = int(sys.stdin.readline())
    if a != 0:
        heapq.heappush(heap,a)
    elif heap:
        print(heapq.heappop(heap))
    else:
        print(0)