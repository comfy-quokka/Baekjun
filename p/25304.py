import sys
X = int(sys.stdin.readline())
N = int(sys.stdin.readline())
for i in range(N):
    tmp1, tmp2 = map(int,sys.stdin.readline().split())
    X -= tmp1*tmp2
if X == 0:
    print('Yes')
else:
    print('No')