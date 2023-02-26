'''
start 20220302
end
'''

import sys

def gcd(a,b):
    while b % a != 0:
        a, b = b % a, a
    return a

n = int(sys.stdin.readline())
pv = int(sys.stdin.readline())
t = -1
for i in range(n-1):
    v = int(sys.stdin.readline())
    k = abs(pv-v)
    if t == -1:
        t = k
    else:
        t = gcd(t, k)
d = []
for i in range(1,int(t**(1/2))+1):
    if t%i == 0:
        d.append(i)
        if (i**2) != t:
            d.append(t//i)
d.sort()
for i in d[1:]:
    print(i,end=' ')