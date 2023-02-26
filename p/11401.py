'''
start 20220305
end
'''

import sys

def cal(a,b,c):
    if b == 1:
        return a%c
    else:
        d = cal(a,b//2,c)
        if b%2 == 0:
            return (d*d)%c
        else:
            return (d*d*a)%c

a,b = map(int,sys.stdin.readline().split())
c = 1000000007
A = 1
B = 1
for i in range(a):
    if i<a-b:
        B *= (i + 1)
        B %= c
    if i<b:
        B*=(i+1)
        B%=c
    A*=(i+1)
    A%=c
print((A*cal(B,c-2,c))%c)