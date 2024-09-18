
class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.ref=None

class Stack:
    def __init__(self) -> None:
        self.head=None

    def isempty(self):
        return self.head is None
    
    def push(self,data:any)->None:
        new_node=Node(data)
        if self.isempty():
            self.head=new_node
            return
        new_node.ref=self.head
        self.head=new_node
    
    def pop(self)->any:
        if self.isempty():
            return None
        data=self.head.data
        self.head=self.head.ref
        return data
    
    def peek(self)->any:
        if self.isempty():
            return None
        return self.head.data