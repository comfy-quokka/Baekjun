import sys

n = int(sys.stdin.readline())
s = {1:0}

for i in range(2,n+1):
    if i%6 == 0:
        s[i] = min(s[i//3],s[i//2],s[i-1])+1
    elif i%3 == 0:
        s[i] = min(s[i//3],s[i-1])+1
    elif i%2 == 0:
        s[i] = min(s[i//2],s[i-1])+1
    else:
        s[i] = s[i-1]+1
print(s[n])