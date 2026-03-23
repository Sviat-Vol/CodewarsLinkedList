class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError
    fir = None
    sec = None
    probe = head
    ind = 0
    last_1 = None
    last_2 = None
    while probe is not None:
        if ind == 0:
            ind = 1
            ne = probe.next
            probe.next = None
            if fir is None:
                fir = probe
                fir.next = None
            else:
                last_1.next = probe
            last_1 = probe
            probe = ne
            continue
        if ind == 1:
            ind = 0
            ne = probe.next
            probe.next = None
            if sec is None:
                sec = probe
                sec.next = None
            else:
                last_2.next = probe
            last_2 = probe
            probe = ne
        ne = None
    return Context(fir, sec)
