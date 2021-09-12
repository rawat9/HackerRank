def reversePrint(llist):
    stack = []
    current = llist
    while current:
        stack.append(current.data)
        current = current.next

    while stack:
        print(stack.pop())