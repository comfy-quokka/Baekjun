'''
start 20220314
end
'''

import sys

n = int(sys.stdin.readline())
l = list(map(int,sys.stdin.readline().split()))

d = [0]

for item in l:
    if item > d[-1]:
        d.append(item)
    else:
        start = 0
        end = len(d)
        while start < end:
            mid = (start+end)//2
            if d[mid] >= item:
                end = mid
            else:
                start = mid+1
        d[end] = item
print(len(d)-1)