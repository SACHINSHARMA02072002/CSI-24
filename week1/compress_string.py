# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby as gb
s=input()
li=[]
for i,j in gb(s):
    x=(len(list(j)))
    y=(int(i))
    li.append((x,y))
print(*li)