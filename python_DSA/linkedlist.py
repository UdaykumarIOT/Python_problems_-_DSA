class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
        
class LinkedList:
    def __init__(self):
        self.head=None
    
    def add_begin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
        
    def add_end(self,data):
        new_node=Node(data)
        n=self.head
        if n is None:
            self.head=new_node
        else:
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    
    def insert_after(self,data,node):
        n=self.head
        if n is None:
            print("LL is Empty")
        
        else:
            while n is not None:
                if n.data==node :
                    break
                n=n.ref
            
            if n is None:
                print(f"ref node {node} not found")
            else:
                new_node=Node(data)
                new_node.ref=n.ref
                n.ref=new_node
        
    
    def insert_before(self,data,node):
        n=self.head
        if n is None:
            print("LL is Empty")
        
        elif n.data==node:
            new_node=Node(data)
            new_node.ref=n
            self.head=new_node
        
        else:
            while n.ref is not None:
                if n.ref.data==node:
                    break
                n=n.ref
            
            if n.ref is None:
                print(f"ref node {node} not found")
            else:
                new_node=Node(data)
                new_node.ref=n.ref
                n.ref=new_node
    
    def delete_begin(self):
        if self.head is None:
            print("LL is Empty")
        
        else:
            self.head=self.head.ref
    
    def delete_end(self):
        if self.head is None:
            print("LL is Empty")
        
        elif self.head.ref is None:
            self.head=None
        
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None
    
    def delete_by_value(self,data):
        if self.head is None:
            print("LL is Empty")
        
        elif self.head.data == data:
            self.head=self.head.ref
        
        else:
            n=self.head
            while n.ref is not None:
                if n.ref.data== data:
                    break
                n=n.ref
            if n.ref is None:
                print("data not found")
            else:
                n.ref=n.ref.ref
    
    def sort(self,reverse=False):
        if self.head is None:
            print("LL is Empty")
        elif self.head.ref is None:
            return
        else:
            if not reverse:
                done=False
                while not done:
                    done=True
                    n=self.head
                    pn=None
                    while n.ref is not None:
                        if n.data > n.ref.data:
                            done=False
                            x=n.ref
                            n.ref=n.ref.ref
                            x.ref=n
                            if pn is not None:
                                pn.ref=x
                            pn=x
                            if n is self.head:
                                self.head=x
                        else:
                            pn=n
                            n=n.ref
            else:
                done=False
                while not done:
                    done=True
                    n=self.head
                    pn=None
                    while n.ref is not None:
                        if n.data < n.ref.data:
                            done=False
                            x=n.ref
                            n.ref=n.ref.ref
                            x.ref=n
                            if pn is not None:
                                pn.ref=x
                            pn=x
                            if n is self.head:
                                self.head=x
                        else:
                            pn=n
                            n=n.ref
    
    def search(self,data):
        if self.head is None:
            print("LL is Empty")
        n=self.head
        index=0
        while n is not None:
            if n.data==data:
                print(f"data found at position { index }")
                return
            n=n.ref
            index +=1
        print("data not found")
        
    def display(self):
        n=self.head
        while n is not None:
            print(f"{n.data} -->",end=" ")
            n=n.ref
        print("Null")
        
    
l=LinkedList()
l.add_end(100)
l.add_end(74)
l.add_end(102)
l.add_end(62)
l.add_end(67)
l.display()
l.sort()
l.display()
l.search(62)