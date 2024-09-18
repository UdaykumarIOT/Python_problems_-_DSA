class Node:
    def __init__(self,data):
        self.data=data
        self.pref=None
        self.nref=None

class DCLL:
    def __init__(self):
        self.head=None
        
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
        
    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            new_node.nref=new_node
            new_node.pref=new_node
            self.head=new_node
        else:
            new_node.nref=self.head
            new_node.pref=self.head.pref
            self.head.pref=new_node
            new_node.pref.nref=new_node
            self.head=new_node
    
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            new_node.nref=new_node
            new_node.pref=new_node
            self.head=new_node
        else:
            new_node.nref=self.head
            new_node.pref=self.head.pref
            self.head.pref=new_node
            new_node.pref.nref=new_node
    
    def add_after(self,data,node):
        if self.isEmpty():
            print("DCLL is Empty")
        else:
            n=self.head
            while True:
                if n.data==node:
                    break
                n=n.nref
                if n is self.head:
                    print("data not found")
                    return
            new_node=Node(data)
            new_node.nref=n.nref
            new_node.pref=n
            n.nref.pref=new_node
            n.nref=new_node
    
    def add_before(self,data,node):
        if self.isEmpty():
            print("DCLL is Empty")
        else:
            n=self.head
            while True:
                if n.data==node:
                    break
                n=n.nref
                if n is self.head:
                    print("data not found")
                    return
            new_node=Node(data)
            new_node.nref=n
            new_node.pref=n.pref
            n.pref.nref=new_node
            n.pref=new_node
            if n is self.head:
                self.head=n.pref
            
    def delete_begin(self):
        if self.isEmpty():
            return
        elif self.head.nref is self.head:
            self.head=None
        else:
            self.head.nref.pref=self.head.pref
            self.head.pref.nref=self.head.nref
            self.head=self.head.nref
    
    def delete_end(self):
        if  self.isEmpty():
            return
        elif self.head.nref is self.head:
            self.head=None
        else:
            n=self.head.pref
            n.pref.nref=self.head
            self.head.pref=n.pref
    
    def delete_by_value(self,data):
        if  self.isEmpty():
            print("DCLL is Empty")
        elif self.head.nref is self.head:
            if self.head.data==data:
                self.head=None
            else:
                print("data not found")
        else:
            n=self.head
            while True:
                if n.data==data:
                    n.pref.nref=n.nref
                    n.nref.pref=n.pref
                    if n is self.head:
                        self.head=n.nref
                    return
                if n.nref is self.head:
                    print("data not found")
                    return
                n=n.nref
                    
    def sort(self,reverse=False):
        if  self.isEmpty():
            return
        elif self.head.nref is self.head:
            return
        else:
            if not reverse:
                done=False
                while not done:
                    done=True
                    n=self.head
                    while n.nref is not self.head:
                        if n.data > n.nref.data:
                            done=False
                            x=n.nref
                            n.nref=x.nref
                            x.nref.pref=n
                            x.nref=n
                            x.pref=n.pref
                            n.pref=x
                            x.pref.nref=x
                            if n is self.head:
                                self.head=x
                        else:
                            n=n.nref
            else:
                done=False
                while not done:
                    done=True
                    n=self.head
                    while n.nref is not self.head:
                        if n.data < n.nref.data:
                            done=False
                            x=n.nref
                            n.nref=x.nref
                            x.nref.pref=n
                            x.nref=n
                            x.pref=n.pref
                            n.pref=x
                            x.pref.nref=x
                            if n is self.head:
                                self.head=x
                        else:
                            n=n.nref
        
    def display(self,reverse=False):
        if self.isEmpty():
            print("None")
        elif self.head.nref is self.head:
            print(self.head.data)
        else:
            if not reverse:
                n=self.head
                while n.nref is not self.head:
                    print(f"{n.data} <===>",end=" ")
                    n=n.nref
                print(n.data)
            else:
                n=self.head.pref
                while n is not self.head:
                    print(f"{n.data} <===>",end=" ")
                    n=n.pref
                print(n.data)
                
dc=DCLL()
dc.add_begin(112)
dc.add_end(11)
dc.add_end(30)
dc.add_end(120)
dc.sort()
dc.sort(1)
dc.display()