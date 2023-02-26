'''
start 20220303
end
'''

import sys

n = int(sys.stdin.readline())
ans = []
for i in range(n):
    tmp = sys.stdin.readline()[:-1]
    s = True
    st = []
    for j in range(len(tmp)):
        if tmp[j] == ')' and len(st) == 0:
            s = False
            break
        elif tmp[j] == ')':
            st.pop()
        else:
            st.append(0)
    if s and len(st) == 0:
        ans.append('YES')
    else:
        ans.append('NO')
for i in range(n):
    print(ans[i])