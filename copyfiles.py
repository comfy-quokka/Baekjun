import shutil

l = [11279,1927,11286,1655]
for x in l:
    a = str(x)+'.py'
    b = 'Classification/22_heapq/'+a
    shutil.copyfile(a,b)