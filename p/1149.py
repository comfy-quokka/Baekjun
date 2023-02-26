import sys
n = int(sys.stdin.readline())
s = []
for i in range(n):
    s.append(list(map(int,sys.stdin.readline().split())))
t0,t1,t2 = 0,0,0
for h in s:
    t0,t1,t2 = min(h[0]+t1,h[0]+t2),min(h[1]+t0,h[1]+t2),min(h[2]+t0,h[2]+t1)
print(min(t0,t1,t2))