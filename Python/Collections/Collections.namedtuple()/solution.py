from collections import namedtuple

n = int(input())
total = 0
Student = namedtuple('Student', input())
for _ in range(n):
    total += int(Student(*list(map(str, input().split()))).MARKS)

print(total/n)
