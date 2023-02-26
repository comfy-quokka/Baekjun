import sys

dp = [0]
n = int(sys.stdin.readline())
ps = 0
for i in range(1,n+1):
    s = int(sys.stdin.readline())
    if i == 1:
        dp.append(s)
    elif i == 2:
        dp.append(dp[1]+s)
    else:
         if dp[-2] > (dp[-3]+ps):
             dp.append(dp[-2]+s)
         else:
             dp.append(dp[-3]+ps+s)
    ps = s
print(dp[-1])