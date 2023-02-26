'''
start 20220304
end
'''

import sys

def check(d):
    global b
    global w
    n = len(d)
    s = 0
    for l in d:
        s+=sum(l)
    if s == len(d)**2:
        b+=1
    elif s == 0:
        w += 1
    else:
        d1,d2,d3,d4 = [],[],[],[]
        for i in range(n//2):
            d1.append(d[i][:n//2])
            d2.append(d[i][n//2:])
            d3.append(d[i+n//2][:n//2])
            d4.append(d[i+n//2][n//2:])
        check(d1)
        check(d2)
        check(d3)
        check(d4)

nn = int(sys.stdin.readline())
data = []

for i in range(nn):
    data.append(list(map(int,sys.stdin.readline().split())))
b = 0
w = 0
check(data)
print(w)
print(b)