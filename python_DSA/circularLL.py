class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
        
class CLL:
    def __init__(self):
        self.head=None
        
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
        
    def add_begin(self,data):
        new_node=Node(data)
        if self.isEmpty():
            new_node.ref=new_node
            self.head=new_node
        else:
            n=self.head
            new_node.ref=self.head
            while n.ref is not self.head:
                n=n.ref
            n.ref=new_node
            self.head=new_node
    
    def add_end(self,data):
        new_node=Node(data)
        if self.isEmpty():
            new_node.ref=new_node
            self.head=new_node
        else:
            n=self.head
            while n.ref is not self.head:
                n=n.ref
            n.ref=new_node
            new_node.ref=self.head
    
    def add_after(self,data,node):
        if self.isEmpty():
            print("CLL is Empty")
        else:
            n=self.head
            while True:
                if n.data==node:
                    break
                if n.ref is self.head:
                    print("data  not found")
                    return
                n=n.ref
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
    
    def add_before(self,data,node):
        if self.isEmpty():
            print("CLL is Empty")
        elif self.head.data==node:
            new_node=Node(data)
            new_node.ref=self.head
            n=self.head
            while n.ref is not self.head:
                n=n.ref
            n.ref=new_node
            self.head=new_node
        else:
            n=self.head
            while n.ref is not self.head:
                if n.ref.data==node:
                    break
                n=n.ref
            if n.ref is self.head:
                print("data not found")
            else:
                new_node=Node(data)
                new_node.ref=n.ref
                n.ref=new_node
    
    def delete_begin(self):
        if self.isEmpty():
            print("CLL is Empty")
        else:
            n=self.head
            while n.ref is not self.head:
                n=n.ref
            if n is self.head:
                self.head=None
            else:
                n.ref=self.head.ref
                self.head=self.head.ref
    
    def delete_end(self):
        if self.isEmpty():
            print("CLL is Empty")
        
        elif self.head.ref==self.head:
            self.head=None
        else:
            n=self.head
            while n.ref.ref is not self.head:
                n=n.ref
            n.ref=self.head
    
    def delete_by_value(self,data):
        if self.isEmpty():
            print("CLL is Empty")
        else:
            if self.head.ref==self.head:
                if self.head.data==data:
                    self.head=None
                else:
                    print("data not found")
            else:
                if self.head.data==data:
                    n=self.head
                    while n.ref is not self.head:
                        n=n.ref
                    n.ref=self.head.ref
                    self.head=self.head.ref
                else:
                    n=self.head
                    while n.ref is not self.head:
                        if n.ref.data==data:
                            break
                        n=n.ref
                    if n.ref is self.head:
                        print("data not found")
                    else:
                        n.ref=n.ref.ref
                        
    def sort(self,reverse=False):
        if self.isEmpty() or self.head.ref==self.head:
            return
        else:
            if not reverse:
                done=False
                while not done:
                    done=True
                    n=self.head
                    while n.ref is not self.head:
                        if n.data > n.ref.data:
                            done=False
                            x=n.ref
                            n.ref=x.ref
                            x.ref=n
                            if n==self.head:
                                m=self.head
                                while m.ref is not self.head:
                                    m=m.ref
                                m.ref=x
                                self.head=x
                            else:
                                y.ref=x
                            y=x
                        else:
                            y=n
                            n=n.ref
            else:
                done=False
            while not done:
                done=True
                n=self.head
                while n.ref is not self.head:
                    if n.data < n.ref.data:
                        done=False
                        x=n.ref
                        n.ref=x.ref
                        x.ref=n
                        if n==self.head:
                            m=self.head
                            while m.ref is not self.head:
                                m=m.ref
                            m.ref=x
                            self.head=x
                        else:
                            y.ref=x
                        y=x
                    else:
                        y=n
                        n=n.ref
        
    
    def display(self):
        if self.isEmpty():
            print("None")
        else:
            n=self.head
            while n.ref is not self.head:
                print(f"{n.data} --->",end=" ")
                n=n.ref
            print(n.data)
        
c=CLL()
c.add_begin(10)
c.add_end(20)
c.add_begin(30)
c.add_after(40,10)
c.add_before(50,20)
c.add_begin(100)
c.sort(reverse=True)
c.display()

        