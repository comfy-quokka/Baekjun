import sys

n = int(sys.stdin.readline())
s = [0,1,1,1,1,1,1,1,1,1]
for _ in range(n-1):
    ps = s.copy()
    for i in range(10):
        if i == 0:
            s[i] = ps[1]
        elif i == 9:
            s[i] = ps[8]
        else:
            s[i] = ps[i+1]+ps[i-1]
print(sum(s)%10**9)