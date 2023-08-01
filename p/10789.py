import sys

s = []
for ii in range(5):
    s.append(list(sys.stdin.readline().strip()))
for ii in range(15):
    for line in s:
        try:
            print(line[ii],end='')
        except:
            continue