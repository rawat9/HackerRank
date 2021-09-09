def insertNodeAtPosition(llist, data, position):
    current = llist
    node = SinglyLinkedListNode(data)  # node to insert

    counter = 0
    while counter != (position - 1):
        current = current.next
        counter += 1

    # current = value at position - 1
    temp = current.next
    current.next = node
    node.next = temp

    return llist