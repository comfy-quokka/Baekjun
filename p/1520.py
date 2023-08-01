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

dp = [(1,1)]

def search(state,mat,dp):
    i,j = state
    num = mat[i][j]
    if mat[i-1][j] < num:
        dp.append((i-1,j))
    if mat[i][j-1] < num:
        dp.append((i,j-1))
    if mat[i+1][j] < num:
        dp.append((i+1,j))
    if mat[i][j+1] < num:
        dp.append((i,j+1))
    return dp

cnt = 0

while dp:
    state = dp.pop()
    if state == (n,m):
        cnt += 1
    else:
        dp = search(state,mat,dp)
print(cnt)
