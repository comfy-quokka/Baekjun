import sys

s = sys.stdin.readlines()
sc = {
    'A+':4.5,
    'A0':4,
    'B+':3.5,
    'B0':3,
    'C+':2.5,
    'C0':2,
    'D+':1.5,
    'D0':1,
    'F':0
         }
ss = 0
cnt = 0
for line in s:
    a,b,c = line.split()
    if c != 'P':
        ss += float(b)*sc[c]
        cnt += float(b)
    else:
        continue
print(ss/cnt)
