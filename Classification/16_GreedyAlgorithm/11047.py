# 20220228

import sys

N, K = list(map(int,sys.stdin.readline().split()))
coin = []
m = 0
for i in range(N):
    v = int(sys.stdin.readline())
    if K >= v:
        coin.append(v)
        m = i
s=0
for j in range(m+1):
    s += K//coin[m-j]
    K%=coin[m-j]
print(s)