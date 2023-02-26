'''
start 20220303
end
'''

import sys

def cnt5(n):
    c=0
    while n >= 5:
        c += n // 5
        n //= 5
    return c
def cnt2(n):
    c=0
    while n >= 2:
        c += n // 2
        n //= 2
    return c

n,k = map(int,sys.stdin.readline().split())
print(min(cnt2(n)-cnt2(k)-cnt2(n-k),cnt5(n)-cnt5(k)-cnt5(n-k)))