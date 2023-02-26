'''
start 20220308
end
'''

import sys

n = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
t = list(map(int,sys.stdin.readline().split()))
d = {}
for x in A:
    if x in d:
        d[x] += 1
    else:
        d[x] = 1
for x in t:
    if x in d:
        print(d[x],end=' ')
    else:
        print(0,end=' ')