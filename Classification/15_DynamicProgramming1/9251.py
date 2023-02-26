import sys

t1 = sys.stdin.readline().strip()
t2 = sys.stdin.readline().strip()

N = len(t1)
M = len(t2)
dp = [[0 for _ in range(N+1)] for __ in range(M+1)]
v = 0
for i in range(M):
    for j in range(N):
        if t1[j] == t2[i]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
    v = max(max(dp[i+1]),v)
print(v)