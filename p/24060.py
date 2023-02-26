import sys

N, K = map(int,sys.stdin.readline().split())
x = list(map(int,sys.stdin.readline().split()))

# dp = [0]
# for i in range(2,N+1):
#     if i%2 == 0:
#         dp.append(dp[i//2-1]*2+i)
#     else:
#         dp.append(dp[i//2]+dp[i//2-1]+i)
# if dp[-1] < K:
#     print(-1)
def func(x):
    global c
    if len(x) == 1:
        return 0
    elif len(x) == 2:
        return 2
    elif len(x)%2 == 0:

if dp[-1] < K:
    print(-1)
else:
    while True:
        if N%2 == 0:
            if dp[N//2-1]*2 < K:
                x.sort()
                print(x[K-dp[N//2-1]*2-1])
                break
            elif dp[N//2-1] <= K:
                N //= 2
                x = x[:N]
                continue
            else:
                N //= 2
                K -= dp[N-1]
                x = x[N:]
                continue
        else:
            if dp[N//2]+dp[N//2-1] < K:
                x.sort()
                print(x[K-dp[N//2]-dp[N//2-1]-1])
                break
            elif dp[N//2] >= K:
                N //= 2
                N += 1
                x = x[:N]
                continue
            else:
                N //= 2
                K -= dp[N]
                x = x[N+1:]
                continue
