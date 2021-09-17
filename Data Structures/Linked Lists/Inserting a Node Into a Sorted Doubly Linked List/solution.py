def sortedInsert(llist, data):
    new_node = DoublyLinkedListNode(data)
    current = llist  # head

    if current.data > new_node.data:
        new_node.next = current
        current.prev = new_node
        current = new_node
        return current

    while current:
        if current.data < new_node.data and current.next == None:
            current.next = new_node
            new_node.prev = current
            new_node.next = None

        elif current.data < new_node.data and current.next.data >= new_node.data:
            temp = current.next
            current.next = new_node
            new_node.next = temp
            temp.prev = new_node

        current = current.next

    return llist
