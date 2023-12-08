import sys

A,B = sys.stdin.readline().split()
B = int(B)
cnt = 0
for i, a in enumerate(reversed(A)):
    if ord(a)<60:
        cnt += B**i*int(a)
    else:
        cnt += B**i*(ord(a)-55)
print(cnt)