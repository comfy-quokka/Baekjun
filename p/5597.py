import sys

l = list(range(1,31))
for i in range(28):
    l.remove(int(sys.stdin.readline()))
for i in range(len(l)):
    print(l[i])