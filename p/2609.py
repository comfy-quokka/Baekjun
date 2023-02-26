'''
start 20220302
end
'''

import sys

a0,b0 = map(int, sys.stdin.readline().split())
a,b = a0,b0
while b%a != 0:
    a,b = b%a,a
print(a)
print(a0*b0//a)