from itertools import permutations

s, n = input().split()

for perm in permutations(sorted(s), int(n)):
    print("".join(perm))
