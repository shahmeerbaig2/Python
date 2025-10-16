def Get(self, Index):
    if Index < 0 or Index >= self.length:
        return None
    temp = self.head
    for _ in range(Index):
        temp = temp.next
    return temp