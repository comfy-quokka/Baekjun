'''
start 20220303
end
'''

import sys

n,k = map(int, sys.stdin.readline().split())
u = 1
d = 1
for i in range(k):
    u *= (n-i)
    d *= (i+1)
print((u//d)%10007)