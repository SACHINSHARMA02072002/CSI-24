from collections import Counter
X = input()
sizes = input()
sizes = map(int, sizes.split())
sizes_dict = Counter(sizes)
N = int(input())
total_sale = 0
for i in range(N):
    s, price = tuple(map(int, input().split()))
    if sizes_dict[s] > 0 : 
        total_sale += price 
        sizes_dict[s] -= 1 
print(total_sale)