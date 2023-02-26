'''
start 20220303
end
'''

import sys

st = []
n = int(sys.stdin.readline())
for i in range(n):
    a = int(sys.stdin.readline())
    if a != 0:
        st.append(a)
    else:
        st.pop()
print(sum(st))