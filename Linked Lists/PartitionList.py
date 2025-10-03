def partition_list(self,x):
    dummy1 = Node(0)
    dummy2 = Node(0)
    prev1 = dummy1
    prev2 = dummy2
    current=self.head
    while current is not None:
        if current.value>=x:
            prev2.next=current
            prev2=prev2.next
        else:
            prev1.next=current
            prev1=prev1.next
        current=current.next
    prev1.next=dummy2.next
    prev2.next=None
    self.head=dummy1.next