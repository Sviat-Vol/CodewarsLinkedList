from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    list_repr = list_repr.split(' -> ')
    if list_repr[0] == 'None':
        return None
    head = Node(int(list_repr[0])) if list_repr[0].isdecimal() else Node(list_repr[0].strip())
    list_repr = list_repr[1:]
    current = head
    while list_repr:
        new_node = Node(int(list_repr[0])) if list_repr[0].strip().isdecimal() else Node(list_repr[0].strip())
        if list_repr[0] == 'None':
            break
        list_repr = list_repr[1:]
        current.next = new_node
        current = new_node
    return head
