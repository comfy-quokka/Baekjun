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

a,b,c = map(int,sys.stdin.readline().split())
print(cal(a,b,c))