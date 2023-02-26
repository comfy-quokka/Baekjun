import sys

n = int(sys.stdin.readline())
for i in range(n):
    k = int(sys.stdin.readline())
    a,b,c=0,1,1
    for _ in range(k):
        a,b,c = b,c,a+b
    print(a)