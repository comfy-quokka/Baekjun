import sys
def cnt(s):
    dp = []
    n = len(s)
    for i in range(n):
        c = 0
        for j in range(i):
            if s[j] < s[i] and c < dp[j]:
                c = dp[j]
        dp.append(c+1)
    return dp
n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
dp_f = cnt(s)
s.reverse()
dp_b = cnt(s)
dp_b.reverse()
c = 0
for i in range(n):
    if dp_b[i]+dp_f[i] > c:
        c = dp_b[i]+dp_f[i]
print(c-1)