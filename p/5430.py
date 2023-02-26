'''
start 20220304
end
'''

import sys
from collections import deque

T = int(sys.stdin.readline())
ans = []
for i in range(T):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    l = deque(sys.stdin.readline()[1:-2].split(','))
    if l == deque(['']):
        l = deque([])
    rev = True
    error = False
    for f in p:
        if f == 'R':
            rev = not rev
        elif f == 'D':
            if not len(l):
                error = True
                break
            elif rev:
                l.popleft()
            else:
                l.pop()
    if error:
        ans.append('error')
    else:
        s = '['
        if len(l) != 0:
            for i in range(len(l)):
                if rev:
                    s+=l[i]+','
                else:
                    s+=l[len(l)-i-1]+','
            s = s[:-1]+']'
        else:
            s = '[]'
        ans.append(s)
for i in range(T):
    print(ans[i])