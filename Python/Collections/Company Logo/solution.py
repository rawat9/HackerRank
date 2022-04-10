from collections import Counter

counter = Counter(sorted(input()))
for char, t in counter.most_common(3):
    print(char, t)
