import sys

l = []
for i in range(5):
    l.append(int(sys.stdin.readline()))
mean = sum(l)/5
for i in range(2):
    l.remove(max(l))
    l.remove(min(l))
print("%d\n%d"%(mean,l[0]))