import sys

m = -1
for i in range(9):
    l = list(map(int,sys.stdin.readline().split()))
    if max(l)>m:
        m = max(l)
        m_loc = [i+1,l.index(m)+1]
print(m)
print(m_loc[0], m_loc[1])