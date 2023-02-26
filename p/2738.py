import sys

N,M = list(map(int,sys.stdin.readline().split()))

A = []
for i in range(N):
    A.append(list(map(int,sys.stdin.readline().split())))
for i in range(N):
    l = list(map(int,sys.stdin.readline().split()))
    for j in range(M):
        A[i][j] += l[j]
for i in range(N):
    for j in range(M):
        print(A[i][j],end=' ')
    print()