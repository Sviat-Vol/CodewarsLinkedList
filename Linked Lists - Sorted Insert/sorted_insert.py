""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    probe = head
    new_node = Node(data)
    last = None
    while probe is not None and probe.data < data:
        last = probe
        probe = probe.next
    if last:
        new_node.next = last.next
        last.next = new_node
    else:
        new_node.next = head
        return new_node
    return head
