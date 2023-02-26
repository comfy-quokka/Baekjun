'''
start 20220305
end
'''

import sys

def check(d):
    global f
    global s
    global t
    n = len(d)
    tot = 0
    df = d[0][0]
    tf = True
    for l in d:
        for c in l:
            if c != df:
                tf = False
                break
    if tf:
        if df == -1:
            f+=1
        elif df == 0:
            s += 1
        else:
            t += 1
    else:
        d1,d2,d3,d4,d5,d6,d7,d8,d9 = [],[],[],[],[],[],[],[],[]
        for i in range(n//3):
            d1.append(d[i][:n//3])
            d2.append(d[i][n//3:n//3*2])
            d3.append(d[i][n//3*2:])
            d4.append(d[i+n//3][:n//3])
            d5.append(d[i+n//3][n//3:n//3*2])
            d6.append(d[i+n//3][n//3*2:])
            d7.append(d[i+n//3*2][:n//3])
            d8.append(d[i+n//3*2][n//3:n//3*2])
            d9.append(d[i+n//3*2][n//3*2:])
        check(d1)
        check(d2)
        check(d3)
        check(d4)
        check(d5)
        check(d6)
        check(d7)
        check(d8)
        check(d9)

nn = int(sys.stdin.readline())
data = []

for i in range(nn):
    data.append(list(map(int,sys.stdin.readline().split())))
f,s,t=0,0,0
check(data)
print(f)
print(s)
print(t)