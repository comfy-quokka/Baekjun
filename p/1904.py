import sys
n = int(sys.stdin.readline())
t1,t2=0,1
for i in range(n):
    t3 = t1+t2
    t1,t2 = t2%15746,t3%15746
print(t2)