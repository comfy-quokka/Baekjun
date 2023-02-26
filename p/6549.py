'''
start 20220308
end
'''

import sys

while True:
    case = list(map(int,sys.stdin.readline().split()))
    if case == [0]:
        break
    n = case[0]
    l = case[1:]
    stack_val = []
    stack_idx = []
    stack_back = []
    m = 0
    for idx, val in enumerate(l):
        b = 0
        while stack_val and stack_val[-1] > val:
            tmp1 = stack_val.pop()
            tmp2 = stack_idx.pop()
            tmp3 = stack_back.pop()
            m = max(m,tmp1*(idx-tmp2+tmp3))
            b+=(tmp3+1)
        stack_val.append(val)
        stack_idx.append(idx)
        stack_back.append(b)
    for idx, val in enumerate(stack_val):
        tmp = (n-stack_idx[idx]+stack_back[idx])*val
        m = max(m,tmp)
    print(m)