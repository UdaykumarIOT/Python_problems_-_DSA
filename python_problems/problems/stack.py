class Node:
    def __init__(self, data=0 , ref=None):
        self.data=data
        self.ref=ref

class Stack:
    def __init__(self):
        self.head=None
    
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
        
    def push(self,data):
        new_node=Node(data,self.head)
        self.head=new_node
    
    def pop(self):
        if self.head is None:
            return "empty"
        else:
            n=self.head
            self.head=n.ref
            n.ref=None
            return n.data
    
    def top(self):
        if self.head is None:
            return "empty"
        else:
            return self.head.data
    
    def display(self):
        if self.head is None:
            print("|___|")
        else:
            n=self.head
            while n is not None:
                print(f"|_{n.data}_|")
                n=n.ref
        
          