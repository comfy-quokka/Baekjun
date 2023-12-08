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
dp = [[0 for _ in range(n+2)] for __ in range(n+2)] 
branch = [(1,1)]

def search(state,mat,branch):
    i,j = state
    num = mat[i][j]
    if mat[i-1][j] <= num:
        branch.append((i-1,j))
    if mat[i][j-1] <= num:
        branch.append((i,j-1))
    if mat[i+1][j] <= num:
        branch.append((i+1,j))
    if mat[i][j+1] <= num:
        branch.append((i,j+1))
    return branch

cnt = 0

while branch:
    state = branch.pop()
    if state == (n,m):
        cnt += 1
    else:
        branch = search(state,mat,branch)
print(cnt)
