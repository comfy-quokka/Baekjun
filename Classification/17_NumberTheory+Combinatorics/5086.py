'''
start 20220302
end
'''

import sys

a,b = map(int,sys.stdin.readline().split())
while a != 0 or b != 0:
    if a%b == 0:
        print('multiple')
    elif b%a == 0:
        print('factor')
    else:
        print('neither')
    a,b = map(int,sys.stdin.readline().split())