n = int(input())
a = []
for ii in range(n-1):
    tmp = ' '*(n-ii-1) + '*'*(2*ii+1) 
    print(tmp)
    a.append(tmp)
print('*'*(2*n-1))
for ii in range(1,n):
    print(a[n-ii-1])