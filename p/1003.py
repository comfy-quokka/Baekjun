import sys

def cal(n):
    return int(((1+5**0.5)**n-(1-5**0.5)**n)/2**n/5**0.5)

n = int(sys.stdin.readline())
for i in range(n):
    k = int(sys.stdin.readline())
    if k == 0:
        print('1 0')
    elif k == 1:
        print('0 1')
    else:
        print(cal(k-1),cal(k))