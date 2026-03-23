from preloaded import Node

def swap_pairs(head):
    if not head or not head.next:
        return head
    im = Node(0)
    im.next = head
    prev = im
    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next
        first.next = second.next
        second.next = first
        prev.next = second
        prev = first
    return im.next
