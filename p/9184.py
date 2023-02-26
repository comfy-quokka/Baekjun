import sys
s = []
while True:
    line = list(map(int,sys.stdin.readline().split()))
    if line == [-1,-1,-1]:
        break
    else:
        s.append(line)
for line in s:
    if line[0] < 1 or line[1] < 1 or line[2] < 1:
        print('w({0}, {1}, {2}) = {3}'.format(line[0],line[1],line[2],1))
    elif line[0] > 20 or line[1] > 20 or line[2] > 20:
        print('w({0}, {1}, {2}) = {3}'.format(line[0],line[1],line[2],2**20))
    elif line[0] <= line[1] or line[0] <= line[2]:
        print('w({0}, {1}, {2}) = {3}'.format(line[0],line[1],line[2],2**line[0]))
    else:
        y = min(line[1],line[2])
        z = max(line[1],line[2])
        bef = [[1 for _ in range(z+1)] for _ in range(y+1)]
        now = [[0 for _ in range(z+1)] for _ in range(y+1)]
        for x in range(line[0]):
            for i in range(y+1):
                for j in range(z+1):
                    if i == 0 or j == 0:
                        now[i][j] = 1
                    else:
                        now[i][j] = bef[i][j]+bef[i][j-1]+bef[i-1][j]-bef[i-1][j-1]
            bef = [c[:] for c in now]
        print('w({0}, {1}, {2}) = {3}'.format(line[0],line[1],line[2],now[-1][-1]))