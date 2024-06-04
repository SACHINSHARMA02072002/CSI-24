# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
n = input()
letters = (input().split())
k = int(input())
combos = list(combinations(letters, k))
num = 0
for i in combos:
    if 'a' in i:
        num += 1
print(num/len(combos))