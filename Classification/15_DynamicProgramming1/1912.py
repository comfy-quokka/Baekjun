import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
nl = [l[0]]
for i in range(1,n):
    nl.append(max(l[i],nl[i-1]+l[i]))
print(max(nl))