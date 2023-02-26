'''
start 20220304
end
'''

import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())
list = deque(list(range(1,n+1)))
ans = '<'
i = 1
while list:
    tmp = list.popleft()
    if i%k != 0:
        list.append(tmp)
    else:
        ans += str(tmp) + ', '
    i+=1
ans = ans[:-2]+'>'
print(ans)