from collections import Counter

total = 0
x = int(input())
sizes = Counter(list(map(int, input().split())))

n = int(input())

for _ in range(n):
    size, price = list(map(int, input().split()))
    if sizes[size] > 0:
        total += price
        sizes.update({size: -1})

print(total)
