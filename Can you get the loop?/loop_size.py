def loop_size(node):
    if node is None:
        return 0
    slow = node
    fast = node
    dots = 0
    
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = node
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next
            start = fast
            fast = fast.next
            dots += 1
            while fast != start:
                dots += 1
                fast = fast.next
            return dots
