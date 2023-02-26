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
        heapq.heappush(heap,(abs(a),a))
    elif heap:
        print(heapq.heappop(heap)[1])
    else:
        print(0)