def reverse(llist):
    first = llist
    second = llist.next

    while second:
        temp = second.next
        second.next = first
        first = second
        second = temp

    llist.next = None
    llist = first
    return llist
