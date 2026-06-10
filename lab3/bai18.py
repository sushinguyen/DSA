class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def bubble_sort_linked_list(head):
    if head is None:
        return None
    swapped = True
    while swapped:
        swapped = False
        current = head
        while current.next is not None:
            if current.val > current.next.val:
                current.val, current.next.val = current.next.val, current.val
                swapped = True
            current = current.next
    return head
def print_linked_list(head):
    res = []
    current = head
    while current:
        res.append(str(current.val))
        current = current.next
    res.append("null")
    return " -> ".join(res)
head = Node(1, Node(3, Node(2)))
sorted_head = bubble_sort_linked_list(head)
print(f"Bài 18: {print_linked_list(sorted_head)}")