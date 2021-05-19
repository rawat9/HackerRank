n = int(input())
list1 = list(input().split())
u = int(input())
list2 = list(input().split())

set1 = set(list1)
set2 = set(list2)
    
print(len(set1.union(set2)))