K = int(input())
list1 = list(input().split())

repetition = {}
for i in list1:
    count = repetition.get(i,0)
    repetition[i] = count + 1                     

for j in repetition.items():
    if j[1] == min(repetition.values()):
        print(j[0])