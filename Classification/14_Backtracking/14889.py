import sys
from itertools import combinations

def cal():
    global min_value
    first = True
    for c in t:
        tmp1 = 0
        tmp2 = 0
        ic = [i for i in range(n) if i not in c]
        tmp1 = sum([s[i][j] for i in c for j in c])
        tmp2 = sum([s[i][j] for i in ic for j in ic])
        if first:
            min_value = abs(tmp1-tmp2)
            first = False
        elif min_value > abs(tmp1-tmp2):
            min_value = abs(tmp1-tmp2)
    
n = int(sys.stdin.readline())
s = []
for i in range(n):
    s.append(list(map(int, sys.stdin.readline().split())))

t = list(combinations(range(n), n//2))
cal()
print(min_value)