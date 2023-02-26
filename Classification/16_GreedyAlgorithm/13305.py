'''
start 20220302
end
'''

import sys

n = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))
c = list(map(int,sys.stdin.readline().split()))

nc = c[0]
nl = 0
s = 0
for i in range(1,n):
    if nc <= c[i]:
        nl += l[i-1]
    else:
        s += nc*(nl+l[i-1])
        nc = c[i]
        nl = 0
s += nc*nl
print(s)