from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():
    head = Node(1)
    nd = head
    for i in range(1, 4):
        if i < 3:
            nxt = Node(i+1)
        else:
            nxt = None
        nd.next = nxt
        nd = nxt
    return head
