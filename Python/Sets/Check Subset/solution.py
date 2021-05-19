T = int(input())

for _ in range(T):
    i = input()
    set1 = set(input().split())
    j = input()
    set2 = set(input().split())
    print(set1.issubset(set2))