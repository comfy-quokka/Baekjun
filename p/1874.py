'''
start 20220303
end
'''

import sys

n = int(sys.stdin.readline())
target = []
for i in range(n):
    target.append(int(sys.stdin.readline()))
test = [1]
ans = ['+']
i = 0
j = 2
pp = True
while j <= n:
    if test and test[-1] == target[i]:
        test.pop()
        ans.append('-')
        i+=1
        continue
    test.append(j)
    ans.append('+')
    j+=1

test.reverse()
if  test == target[i:]:
    for i in range(len(ans)):
        print(ans[i])
    for i in range(len(test)):
        print('-')
else:
    print('NO')