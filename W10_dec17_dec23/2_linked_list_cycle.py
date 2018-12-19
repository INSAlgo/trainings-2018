def has_cycle(head):
    seen = set()
    while head.next is not None:
        if id(head.next) in seen:
            return True
        seen.add(id(head.next))
        head = head.next
    return False
