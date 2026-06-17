class Node:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

def insertion_sort_linked_list(head):
    dummy = Node(0)
    curr = head
    
    while curr is not None:
        next_temp = curr.next 
        prev = dummy
        while prev.next is not None and prev.next.data < curr.data:
            prev = prev.next
            

        curr.next = prev.next
        prev.next = curr
        

        curr = next_temp
        
    return dummy.next
def print_list(node):
    res = []
    while node:
        res.append(str(node.data))
        node = node.next
    print(" -> ".join(res) + " -> null")
head = Node(3, Node(1, Node(2)))
print("Trước sắp xếp:")
print_list(head)

sorted_head = insertion_sort_linked_list(head)
print("Sau sắp xếp:")
print_list(sorted_head)