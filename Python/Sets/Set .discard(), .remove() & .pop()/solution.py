n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    args = input().split()
    if args[0] == 'pop':
        s.pop()
    elif args[0] == 'remove':
        s.remove(int(args[1]))
    elif args[0] == 'discard':
        s.discard(int(args[1]))

print(sum(s))

