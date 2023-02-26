'''
start 20220304
end
'''

import sys
from collections import deque

n = int(sys.stdin.readline())
stack = deque([])
for i in range(n):
    a = sys.stdin.readline().split()
    if a[0] == 'push_back':
        stack.append(a[1])
    elif a[0] == 'push_front':
        stack.appendleft(a[1])
    elif a[0] == 'pop_back':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif a[0] == 'pop_front':
        if stack:
            print(stack.popleft())
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(stack))
    elif a[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif a[0] == 'back':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif a[0] == 'front':
        if stack:
            print(stack[0])
        else:
            print(-1)
