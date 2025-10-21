class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()

def reverse_string(string):
    
    new_stack_list=Stack()
    
    reversed_string=""
    
    
    for char in string:
        new_stack_list.push(char)
    
    while not new_stack_list.is_empty():
        reversed_string+=new_stack_list.pop()
    
    return reversed_string
        
       
            





my_string = 'hello'

print ( reverse_string(my_string) )




