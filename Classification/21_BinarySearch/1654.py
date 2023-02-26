'''
start 20220308
end 20220310
'''

import sys

n,k = map(int, sys.stdin.readline().split())
length = []
for i in range(n):
    tmp = int(sys.stdin.readline())
    length.append(tmp)
end = sum(length)//n
start = 1
while True:
    cnt = 0
    mid = (start+end)//2
    for xi in length:
        cnt += (xi//mid)
    if cnt >= k and start >= end:
        break
    elif cnt < k:
        end = mid-1
    else:
        start = mid+1
print(mid)