import sys
n = int(sys.stdin.readline())
lm=[]
for i in range(n):
    line = list(map(int,sys.stdin.readline().split()))
    lm.insert(0,0)
    lm.insert(i+1,0)
    lm = [line[j]+max(lm[j+1],lm[j]) for j in range(i+1)]
print(max(lm))