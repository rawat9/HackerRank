from collections import deque

n = int(input())

for _ in range(n):
    size = int(input())
    blocks = deque(map(int, input().split()))

    for c in sorted(blocks, reverse=True):
        if blocks[-1] == c:
            blocks.pop()
        elif blocks[0] == c:
            blocks.popleft()
        else:
            print('No')
            break
    else:
        print('Yes')
