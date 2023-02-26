import sys

n,k = map(int,sys.stdin.readline().split())
s =[[0,0]]
for i in range(n):
    s.append(list(map(int, sys.stdin.readline().split())))
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,k+1):
        w = s[i][0]
        v = s[i][1]
        if j<w:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(v+dp[i-1][j-w],dp[i-1][j])
print(dp[n][k])