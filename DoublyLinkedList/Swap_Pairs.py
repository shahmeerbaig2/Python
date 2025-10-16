def swap_pairs(self):
    if self.length<2:
        return
    Dummy = Node(0)
    Dummy.next=self.head
    prev=Dummy
    first=self.head
    while first and first.next:
        second=first.next
        first.next=second.next
        second.next.prev=first
        prev.next=second
        secon