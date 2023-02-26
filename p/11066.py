'''
start 20220315
end
'''

import sys

n = int(sys.stdin.readline())
ans = []

for _ in range(n):
    t = int(sys.stdin.readline())
    l = list(map(int, sys.stdin.readline().split()))
    dp = [[0 for __ in range(t)] for ___ in range(t)]
    m = [[0 for __ in range(t)] for ___ in range(t)]
    for i in range(t):
        m[i][i] = i
    for ii in range(1, t):
        for i in range(0, t-ii):
            j = i + ii
            tmp = []
            mi = 100000000000000000
            for k in range(max(m[i][j-1],i),min(m[i+1][j]+1,j)):
                if k >= t-1:
                    break
                if mi > dp[i][k]+dp[k+1][j]:
                    mi = dp[i][k]+dp[k+1][j]
                    m[i][j] = k
            dp[i][j] = mi+sum(l[i:j+1])
    ans.append(dp[0][-1])
for i in range(n):
    print(ans[i])