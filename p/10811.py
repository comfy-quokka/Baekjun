import sys

N, M = map(int, sys.stdin.readline().split())
box = list(range(N))
for ii in range(M):
    a,b = map(int, sys.stdin.readline().split())
    if a!=1:
        box[a-1:b] = box[b-1:a-2:-1]
    else:
        box[a-1:b] = box[b-1::-1]

[print(ball+1,end =' ') for ball in box]