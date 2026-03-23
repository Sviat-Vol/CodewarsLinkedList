def stringify(node):
    txt = ''
    next_probe = node
    while next_probe:
        txt += str(next_probe.data) + ' -> '
        next_probe = next_probe.next
    txt += 'None'
    return txt
