def compare_lists(llist1, llist2):
    while True:
        # if both => null i.e previous nodes being identical
        if not llist1 and not llist2:
            return 1
        
        # if only one node is null OR data differs
        if bool(llist1) != bool(llist2) or llist1.data != llist2.data: 
            return 0
        
        llist1 = llist1.next
        llist2 = llist2.next
