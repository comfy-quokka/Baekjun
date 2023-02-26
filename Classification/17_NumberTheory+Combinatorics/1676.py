'''
start 20220303
end
'''

import sys

n = int(sys.stdin.readline())
c = 0
while n >= 5:
    c += n//5
    n //= 5
print(c)