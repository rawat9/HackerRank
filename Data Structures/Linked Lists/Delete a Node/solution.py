def deleteNode(llist, position):
    current = llist
    if position == 0:
        return current.next

    counter = 0
    while counter != (position - 1):
        current = current.next
        counter += 1

    node = current.next
    current.next = node.next
    return llist