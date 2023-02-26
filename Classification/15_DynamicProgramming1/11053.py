import sys

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
dp = []
for i in range(n):
    c = 0
    for j in range(i):
        if s[j] < s[i] and c < dp[j]:
            c = dp[j]
    dp.append(c+1)
print(max(dp))