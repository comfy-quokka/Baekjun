import sys

n = int(sys.stdin.readline())
s = [0]
pc = 0
for i in range(n):
    c = int(sys.stdin.readline())
    if i == 0:
        s.append(c)
        k = 1
    else:
        if k == 0:
            s.append(c+s[-1])
            k = 1
        elif k == 1:
            s.append(c+s[-1])
            k = 2
        else:
            tmp = [s[-1],s[-2]+c,s[-3]+pc+c]
            s.append(max(tmp))
            k = tmp.index(max(tmp))
    pc = c
print(s[-1])