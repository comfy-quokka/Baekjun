'''
start 20220316
end
'''

import sys

n,m = map(int, sys.stdin.readline().split())
mat = [[10001]*(n+2)]
for i in range(n):
    tmp = list(map(int,sys.stdin.readline().split()))
    mat.append([10001]+tmp+[10001])
mat.append([10001]*(n+2))

dp = [[0 for _ in range(m+2)] for __ in range(n+2)]

def DFS(x,y):



i = 1
j = 1
branch = []
dp[1][1]=1
while True:
    step = []
    # print(i,j)
    if mat[i][j] > mat[i][j+1]:
        step.append((i,j+1,1))
    if mat[i][j] > mat[i][j-1]:
        step.append((i,j-1,2))
    if mat[i][j] > mat[i-1][j]:
        step.append((i-1,j,3))
    if mat[i][j] > mat[i+1][j]:
        step.append((i+1,j,4))
    branch.append(step)

    if not branch[-1]:
        branch.pop()
    if not branch:
        break
    # print(branch)
    i,j,d = branch[-1].pop()
    if not branch[-1]:
        branch.pop()
    dp[i][j] += 1
    # if d == 1:
    #     dp[i][j] += dp[i][j-1]
    # elif d == 2:
    #     dp[i][j] += dp[i][j+1]
    # elif d == 3:
    #     dp[i][j] += dp[i+1][j]
    # else:
    #     dp[i][j] += dp[i-1][j]
    # print('-----')
    # for k in dp:
    #     print(k)
    # print('-----')

# for i in dp:
#     print(i)
print(dp[n][m])