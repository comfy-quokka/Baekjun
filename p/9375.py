'''
start 20220303
end
'''

import sys

n = int(sys.stdin.readline())
ans=[]
for i in range(n):
    w = int(sys.stdin.readline())
    dict = {}
    for j in range(w):
        c = sys.stdin.readline().split()
        if c[1] not in dict:
            dict[c[1]] = 1
        else:
            dict[c[1]] += 1
    tmp = 1
    for v in dict.values():
        tmp *= (v+1)
    ans.append(tmp)

for i in range(n):
    print(ans[i]-1)