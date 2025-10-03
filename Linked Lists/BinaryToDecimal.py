def binary_to_decimal(self):
    num=0
    current=self.head
    while current:
        num=num*2+current.value
        current=current.next
    return num