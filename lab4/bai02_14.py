class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def selection_sort_linked(head):
    sorted_head = None
    sorted_tail = None
    current = head
    while current is not None:
        min_prev = None
        min_node = current
        prev = current
        node = current.next
        while node:
            if node.val < min_node.val:
                min_prev = prev
                min_node = node
            prev = node
            node = node.next
        if min_prev:
            min_prev.next = min_node.next
        else:
            current = min_node.next
        min_node.next = None
        if not sorted_head:
            sorted_head = sorted_tail = min_node
        else:
            sorted_tail.next = min_node
            sorted_tail = min_node
    return sorted_head

def make_list(vals):
    head = None
    for v in reversed(vals):
        n = Node(v); n.next = head; head = n
    return head

def print_list(head):
    res = []
    while head:
        res.append(head.val); head = head.next
    print(res)

print_list(selection_sort_linked(make_list([3, 1, 2])))  # [1, 2, 3]
