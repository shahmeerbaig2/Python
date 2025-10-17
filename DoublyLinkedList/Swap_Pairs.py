def swap_pairs(self):
    if self.length<=1:
        return None
    Dummy=Node(0)
    Dummy.next=self.head
    prev=Dummy
    first=self.head
        
    while first and first.next:
        second=first.next
        first.next=second.next
        second.next=first
        second.next.prev=first
            
        prev.next=second
        second.prev=prev
        prev=first
        first=first.next
    self.head=Dummy.next
    return