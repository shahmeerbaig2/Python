def reverse_between(self,start_node,end_node):
    Dummy.next=Node(0)
    Dummy=self.head
    prev_node=Dummy
    
    for i in range(start_node):
        prev_node=prev_node.next
    current=prev_node.next

    for i in range(end_node-start_node):
        node_to_move=current.next
        current.next=node_to_move.next
        node_to_move.next=prev_node.next
        prev_node.next=node_to_move
    self.head=Dummy.next