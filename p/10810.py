import sys

N, M = map(int, sys.stdin.readline().split())
box = [0]*N
for ii in range(M):
    a,b,c = map(int, sys.stdin.readline().split())
    box[a-1:b] = [c]*(b-a+1)
[print(ball,end =' ') for ball in box]