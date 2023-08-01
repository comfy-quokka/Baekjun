import sys

N, M = map(int, sys.stdin.readline().split())
box = list(range(N))
for ii in range(M):
    a,b = map(int, sys.stdin.readline().split())
    box[a-1], box[b-1] = box[b-1],box[a-1]
[print(ball+1,end =' ') for ball in box]