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
l = list(map(int,sys.stdin.readline().split()))
base = l[0]
for i in range(1,n):
    g = gcd(base,l[i])
    print(str(base//g)+'/'+str(l[i]//g))