class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    probe = head
    while probe and probe.next:
        if probe.next.data == probe.data:
            probe.next = probe.next.next
            continue
        probe = probe.next
    return head
