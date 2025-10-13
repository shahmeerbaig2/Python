def pop(self):
    if self.length == 0:
        return 0
    temp=self.tail
    if self.length ==1:
        self.head = None
        self.tail = None
    else:
        self.tail=self.tail.prev
        self.tail.next=None
        temp.prev=None
    self.length -= 1
    return temp