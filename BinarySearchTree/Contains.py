def contains(self,value):
    if self.root == None:
        return None
    temp=self.root
    while temp is not None:
        if temp.value<value:
            if temp.left ==value:
                return temp.left.value
            temp=temp.left
        elif temp.value>value:
            if temp.right == value:
                return temp.right.value
            temp=temp.right
        else:
            return temp.value
            
