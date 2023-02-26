'''
start 20220302
end
'''

import sys

n = int(sys.stdin.readline())
f = list(map(int,sys.stdin.readline().split()))
f.sort()
if n != 1:
    print(f[0]*f[-1])
else:
    print(f[0]**2)