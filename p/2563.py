import sys

N = int(sys.stdin.readline())

B = set()
for i in range(N):
    x,y = map(int,sys.stdin.readline().split())
    for j in range(10):
        for k in range(10):
            B.add(1000000+1000*(x+j)+y+k)
print(len(B))