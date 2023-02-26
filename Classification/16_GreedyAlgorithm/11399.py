# 20220228

import sys

str = sys.stdin.readline()
t = 0
s = 0
psi = 0
m = False
for i in range(len(str)):
    if str[i] == '-':
        if m == True:
            t -= (int(s)+int(str[psi:i]))
        else:
            t += (int(s)+int(str[psi:i]))
            m = True
        s = 0
        psi = i + 1
    elif str[i] == '+':
        s += int(str[psi:i])
        psi = i + 1
if str[psi] == '-':
    t -= int(str[psi:])
elif m == True:
    t -= (int(s)+int(str[psi:]))
else:
    t += (int(s)+int(str[psi:]))
print(t)

