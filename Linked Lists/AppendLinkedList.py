class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def Append(self,value):
      new_node = Node(value)
      if self.head is None:
        self.head = new_node
        self.tail = new_node
      else:
        self.tail.next = new_node
        self.tail = new_node
      self.length += 1
    def pop(self):
       if self.length == 0:
        return None
       temp = self.head
       pre = self.head
       while(temp.next):
        pre = temp
        temp = temp.next
       self.tail = pre
       self.tail.next = None
       self.length -= 1
       if self.length == 0:
        self.head = None
        self.tail = None
       return temp

    def print_list(self):
     temp = self.head
     while temp is not None:
        print(temp.value)
        temp = temp.next

    def Pop(self):
      if self.length == 0:
        return None
      temp = self.head
      pre = self.head
      while(temp.next):
          pre = temp
          temp = temp.next
      self.tail = pre
      self.tail.next = None
      self.length -= 1
      if self.length == 0:
        self.head = None
        self.tail = None
      return temp.value
    
    def Prepend(self,value):
      new_node = Node(value)
      if self.head is None:
          self.head = new_node
          self.tail = new_node
      else:
          new_node.next = self.head
          self.head = new_node
      self.length += 1

    def PopFirst(self):
      if self.length == 0:
          return None
      temp = self.head
      self.head = self.head.next
      temp.next = None
      self.length -= 1
      if self.length == 0:
          self.head = None
          self.tail = None
      return temp

    def Get(self, Index):
      if Index < 0 or Index >= self.length:
          return None
      temp = self.head
      for _ in range(Index):
          temp = temp.next
      return temp
    
    def Set(self, index, Value):
      temp = self.Get(index)
      if temp:
          temp.value = Value
          return True
      return False
    
    def Insert(self,index,value):
      if index < 0 or index > self.length:
          return False
      if index == 0:
          return self.Prepend(value)
      if index == self.length:
          return self.Append(value)
      new_node = Node(value)
      temp = self.Get(index - 1)
      new_node.next = temp.next
      temp.next = new_node
      self.length += 1
      return True




my_linked_list = LinkedList(0)
my_linked_list.Append(2)



print(my_linked_list.print_list())
print(my_linked_list.Insert(1, 1))
print(my_linked_list.print_list())
# # print(my_linked_list.Pop())

# print(my_linked_list.Prepend(6))
# # print(my_linked_list.print_list())
# # print(my_linked_list.PopFirst())
# # print(my_linked_list.print_list())

# print(my_linked_list.Get(2))
# print(my_linked_list.Set(0, 99))
# print(my_linked_list.print_list())
