'''
start 20220310
end
'''

import sys

n,m = map(int,sys.stdin.readline().split())
length = list(map(int,sys.stdin.readline().split()))
end = max(length)-1
start = 0

while True:
    mid = (start+end)//2
    c = [x-mid for x in length if x>mid]
    if sum(c) >= m and start >= end:
        break
    elif sum(c) >= m:
        start = mid+1
    else:
        end = mid-1
print(mid)