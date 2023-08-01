import sys

s = list(sys.stdin.readline().strip())
print(1 if list(reversed(s))==s else 0)