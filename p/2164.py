'''
start 20220304
end
'''

import sys
from collections import deque

n = int(sys.stdin.readline())
list = deque(list(range(1,n+1)))
k = 1
while len(list) != 1:
    if k:
        list.popleft()
        k = 0
    else:
        list.append(list.popleft())
        k = 1

print(list[0])
