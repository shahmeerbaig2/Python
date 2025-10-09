class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


my_linked_list = DoublyLinkedList(4)
my_linked_list = DoublyLinkedList(5)


print(my_linked_list.head.value)
