def insertNodeAtTail(head, data):
    current = head
    new_node = SinglyLinkedListNode(data)
    if head:
        while current.next != None:
            current = current.next
        current.next = new_node
    else:
        head = new_node

    return head