class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head, prev=None):
    if head is None:
        return
    if head.next is None:
        head.next = prev
        return head
    else:
        next = head.next
        head.next = prev
        return reverse(next, head)
