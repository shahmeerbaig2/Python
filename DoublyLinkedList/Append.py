def append(self,value):
    if self.head is None:
        self.head = Node(value)
        self.tail = self.head
    else:
        new_node = Node(value)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
    self.length += 1