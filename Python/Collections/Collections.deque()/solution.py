from collections import deque

d = deque()
n = int(input())

for _ in range(n):
    arg = tuple(map(str, input().split()))
    if arg[0] == 'append':
        d.append(arg[1])
    elif arg[0] == 'appendleft':
        d.appendleft(arg[1])
    elif arg[0] == 'pop':
        d.pop()
    elif arg[0] == 'popleft':
        d.popleft()

print(" ".join(d))
