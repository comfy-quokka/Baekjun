'''
start 20220302
end
'''

import sys

n = int(sys.stdin.readline())
c = []
for i in range(n):
    a0, b0 = map(int, sys.stdin.readline().split())
    a, b = a0, b0
    while b % a != 0:
        a, b = b % a, a
    c.append(a0*b0//a)
for x in c:
    print(x)