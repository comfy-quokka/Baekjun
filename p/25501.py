import sys

def recursion(s, l, r):
    global c
    c += 1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

N = int(sys.stdin.readline())
for i in range(N):
    c = 0
    print(isPalindrome(sys.stdin.readline()[:-1]),c)