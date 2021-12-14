from itertools import combinations_with_replacement

S, r = input().split()

for comb in combinations_with_replacement(sorted(S), int(r)):
    print("".join(comb))
