M = int(input())
list1 = list(input().split())

N = int(input())
list2 = list(input().split())

set1 = set(list1)
set2 = set(list2)

print('\n'.join(sorted(set1.symmetric_difference(set2), key=int)))