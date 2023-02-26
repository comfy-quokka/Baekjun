'''
start 20220307
end
'''

import sys

def mul(n):
    global stack
    if n == 1:
        return [[1,1],[1,0]]
    elif n in stack:
        return stack[n]
    else:
        [[a,b],[c,d]] = mul(n//2)
        t = [[(a*a+b*c)%1000000007,(a*b+b*d)%1000000007],
             [(a*b+b*d)%1000000007,(c*b+d*d)%1000000007]]
        if n%2 == 0:
            stack[n] = t
            return stack[n]
        else:
            stack[n] = [[(t[0][0]+t[0][1])%1000000007,t[0][0]],
                        [t[0][0],t[0][1]]]
            return stack[n]


n = int(sys.stdin.readline())
stack = {}
A = mul(n)
print(A[0][1])