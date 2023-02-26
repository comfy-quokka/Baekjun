'''
start 20220303
end
'''

import sys

n = int(sys.stdin.readline())
stack = []
for i in range(n):
    a = sys.stdin.readline().split()
    if a[0] == 'push':
        stack.append(a[1])
    elif a[0] == 'pop':
        if stack == []:
            print(-1)
        else:
            print(stack.pop())
    elif a[0] == 'size':
        print(len(stack))
    elif a[0] == 'empty':
        if stack == []:
            print(1)
        else:
            print(0)
    elif a[0] == 'top':
        if stack == []:
            print(-1)
        else:
            print(stack[-1])