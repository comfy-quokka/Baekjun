import sys

N,k = map(int,sys.stdin.readline().split())
x = list(map(int,sys.stdin.readline().split()))
x.sort(reverse=True)
print(x[k-1])