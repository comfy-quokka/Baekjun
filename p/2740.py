'''
start 20220306
end
'''

import sys

n1, m1 = map(int,sys.stdin.readline().split())
A = []
for i in range(n1):
    A.append(list(map(int,sys.stdin.readline().split())))
n2, m2 = map(int,sys.stdin.readline().split())
B = []
for i in range(n2):
    B.append(list(map(int,sys.stdin.readline().split())))
ans = []
for i in range(n1):
    for j in range(m2):
        c = 0
        for k in range(m1):
            c += A[i][k]*B[k][j]
        print(c,end=' ')
    print()