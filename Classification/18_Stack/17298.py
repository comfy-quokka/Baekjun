'''
start 20220304
end
'''

import sys

n = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))

stack = []
ans = []
for i in range(n):
    while stack and stack[-1][0] < l[i]:
        ans.append((l[i],stack.pop()[1]))
    stack.append((l[i],i))

for i in range(len(stack)):
    ans.append((-1,stack.pop()[1]))

ans.sort(key=lambda x: x[1])

for i in range(n):
    if i < len(ans):
        print(ans[i][0],end=' ')
    else:
        print(-1,end=' ')