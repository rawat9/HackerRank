from collections import Counter

x = int(input())
sizes = Counter(list(map(int, input().split())))

n = int(input())
for _ in range(n):
    size, price = list(map(int, input().split()))
	
print(sizes)
