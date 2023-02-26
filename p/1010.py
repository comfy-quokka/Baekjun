'''
start 20220303
end
'''

import sys

def c(a,b):
    r = 1
    for i in range(b):
        r*=((a-i)/(i+1))
    return round(r)

n = int(sys.stdin.readline())
ans = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    ans.append(c(b,a))
for i in range(n):
    print(ans[i])