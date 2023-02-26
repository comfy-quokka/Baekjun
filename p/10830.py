'''
start 20220307
end
'''

import sys

def m(A,B):
    n = len(A)
    ans = []
    for i in range(n):
        tmp = []
        for j in range(n):
            c = 0
            for k in range(n):
                c += A[i][k]*B[k][j]
            tmp.append(c%1000)
        ans.append(tmp)
    return ans

def power(A,B):
    if B == 1:
        ans = []
        for i in range(len(A)):
            tmp = []
            for j in range(len(A)):
                tmp.append(A[i][j]%1000)
            ans.append(tmp)
        return ans
    else:
        if B%2 == 0:
            return power(m(A,A),B//2)
        else:
            return m(power(m(A,A),B//2),A)

n,B = map(int,sys.stdin.readline().split())
A = []
for i in range(n):
    A.append(list(map(int,sys.stdin.readline().split())))
ans = power(A,B)
for i in range(n):
    for j in range(n):
        print(ans[i][j],end=' ')
    print()