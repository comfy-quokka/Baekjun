'''
start 20220305
end
'''

import sys

def check(d):
    global stack
    n = len(d)
    s = 0
    for l in d:
        s+=sum(l)
    if s == len(d)**2:
        stack.append(1)
    elif s == 0:
        stack.append(0)
    else:
        d1,d2,d3,d4 = [],[],[],[]
        for i in range(n//2):
            d1.append(d[i][:n//2])
            d2.append(d[i][n//2:])
            d3.append(d[i+n//2][:n//2])
            d4.append(d[i+n//2][n//2:])
        stack.append('(')
        check(d1)
        check(d2)
        check(d3)
        check(d4)
        stack.append(')')

nn = int(sys.stdin.readline())
data = []

for i in range(nn):
    data.append(list(map(int,str(sys.stdin.readline()[:-1]))))
stack = []
check(data)
for i in range(len(stack)):
    print(stack[i],end='')