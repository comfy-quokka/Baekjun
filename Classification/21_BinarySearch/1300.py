'''
start 20220311
end
'''

import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
start = 1
end = n**2
p = 0
while True:
    mid = (start+end)//2
    a = int(mid**(1/2))
    c = 0
    t = 0
    for i in range(1,a+1):
        if i**2 > mid:
            a = i-1
            break
        c += min(mid//i,n)
        if mid%i==0 and mid//i <= n:
            t+=1
    c *= 2
    c -= a**2
    if a**2 == mid:
        t = t*2-1
    else:
        t *= 2
    if t and c-t<k and c>=k:
        break
    elif c >= k:
        end = mid-1
    else:
        start = mid+1
print(mid)