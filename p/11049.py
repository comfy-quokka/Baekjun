'''
start 20220315
end
'''

import sys

n = int(sys.stdin.readline())
l = []
ans = []

for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    l.append((a,b))

dp = [[0 for __ in range(n)] for ___ in range(n)]
for ii in range(1, n):
    for i in range(0, n-ii):
        j = i + ii
        tmp = []
        mi = False
        for k in range(i,j):
            value = dp[i][k]+dp[k+1][j]+l[i][0]*l[j][1]*l[k][1]
            if not mi:
                mi = value
            mi = min(mi,value)
        dp[i][j] = mi

print(dp[0][-1])