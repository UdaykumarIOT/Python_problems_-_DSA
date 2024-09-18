class Node:
    def __init__(self,data):
        self.data=data
        self.pref=None
        self.nref=None
    
class DLL:
    def __init__(self):
        self.head=None
    
    def add_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.nref is not None:
                n=n.nref
            n.nref=new_node
            new_node.pref=n
    
    def add_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            new_node.nref=self.head
            self.head.pref=new_node
            self.head=new_node
        
    def add_after(self,data,node):
        if self.head is None:
            print("DLL is Empty")
        else:
            n=self.head
            while n is not None:
                if n.data==node:
                    break
                n=n.nref
            if n is None:
                print("data not found")
            else:
                new_node=Node(data)
                new_node.nref=n.nref
                new_node.pref=n
                n.nref=new_node
                if new_node.nref is not None:
                    new_node.nref.pref=new_node
    
    def add_before(self,data,node):
        if self.head is None:
            print("DLL is Empty")
        else:
            n=self.head
            while n is not None:
                if n.data==node:
                    break
                n=n.nref
            if n is None:
                print("data not found")
            else:
                new_node=Node(data)
                if n is self.head:
                    new_node.nref=n
                    n.pref=new_node
                    self.head=new_node
                else:
                    new_node.nref=n
                    new_node.pref=n.pref
                    n.pref.nref=new_node
                    n.pref=new_node
    
    def delete_begin(self):
        n=self.head
        if n is None:
            print("DLL is Empty")
        elif n.nref is None:
            self.head=None
        else:
            n.nref.pref=None
            self.head=n.nref
    
    def delete_end(self):
        n=self.head
        if n is None:
            print("DLL is Empty")
        elif n.nref is None:
            self.head=None
        else:
            while n.nref is not None:
                n=n.nref
            n.pref.nref=None
    
    def delete_by_value(self,data):
        n=self.head
        if n is None:
            print("DLL is Empty")
        elif n.data==data:
            n.nref.pref=None
            self.head=n.nref
        else:
            n=n.nref
            while n is not None:
                if n.data==data:
                    break
                n=n.nref
            if n is None:
                print("data not found")
            else:
                if n.nref is None:
                    n.pref.nref=None
                else:
                    n.pref.nref=n.nref
                    n.nref.pref=n.pref
        
    def sort(self,reverse=False):
        if self.head is None:
            print("DLL is Empty")
        elif self.head.nref is None:
            return
        else:
            if not reverse:
                done=False
                while not done:
                    done=True
                    n=self.head
                    while n.nref is not None:
                        if n.data > n.nref.data:
                            done=False
                            x=n.nref
                            n.nref=x.nref
                            if x.nref is not None:
                                x.nref.pref=n
                            x.nref=n
                            x.pref=n.pref
                            n.pref=x
                            if x.pref is not None:
                                x.pref.nref=x
                            else:
                                self.head=x
                        else:
                            n=n.nref
            else:
                done=False
                while not done:
                    done=True
                    n=self.head
                    while n.nref is not None:
                        if n.data < n.nref.data:
                            done=False
                            x=n.nref
                            n.nref=x.nref
                            if x.nref is not None:
                                x.nref.pref=n
                            x.nref=n
                            x.pref=n.pref
                            n.pref=x
                            if x.pref is not None:
                                x.pref.nref=x
                            else:
                                self.head=x
                        else:
                            n=n.nref
    
    def search(self,data):
        if self.head is None:
            print("DLL is Empty")
        else:
            n=self.head
            index=0
            while n is not None:
                if n.data==data:
                    print(f"data found in position {index}")
                    return
                n=n.nref
                index += 1
            print("data not found")
            
    
    def display(self,reverse=False):
        n=self.head
        if not reverse:
            while n is not None:
                print(f"{n.data} <===>",end=" ")
                n=n.nref
            print("Null")   
        else:
            if n is None:
                print("Null")
            else:
                while n.nref is not None:
                    n=n.nref
                while n is not None:
                    print(f"{n.data} <===>",end=" ")
                    n=n.pref
                print("Null")
        
l=DLL()
l.add_end(10)
l.add_end(20)
l.add_end(30)
l.add_begin(5)
l.add_begin(2)
l.sort(reverse=1)
l.display()
l.delete_by_value(20)
l.display()
l.search(10)