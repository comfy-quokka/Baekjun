'''
start 20220308
end
'''

import sys

n = int(sys.stdin.readline())
A = set(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
t = list(map(int,sys.stdin.readline().split()))
for k in t:
    if k in A:
        print(1)
    else:
        print(0)