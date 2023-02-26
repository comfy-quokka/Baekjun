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
    return max(dp)

n = int(sys.stdin.readline())
l = []
s = []
for i in range(n):
    t1,t2 = map(int, sys.stdin.readline().split())
    l.append((t1,t2))
l = sorted(l,key = lambda x : x[0])
s = [item[1] for item in l]
k = cnt(s)
print(n-k)