from collections import Counter

t = int(input())

d = Counter(input() for _ in range(t))
print(len(set(d)))
print(*d.values())