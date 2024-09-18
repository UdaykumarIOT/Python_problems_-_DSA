class tree:
    def __init__(self,data=None):
        self.data=data
        if self.data is not None:
            self.left=tree()
            self.right=tree()
        else:
            self.left=None
            self.right=None
    
    def isEmpty(self):
        return (self.data == None)
    
    def insert(self,data):
        if self.isEmpty():
            self.data=data
            self.left=tree()
            self.right=tree()
        
        elif data < self.data:
            self.left.insert(data)
        
        elif data > self.data:
            self.right.insert(data)
        
        else:
            return
    
    def search(self,data):
        if self.isEmpty():
            print("data not found")
            return
        elif data == self.data:
            print("data found")
            return
        elif data < self.data:
            self.left.search(data)
        else:
            self.right.search(data)
    
    def isleaf(self):
        return ((self.left.isEmpty()) and (self.right.isEmpty()))
        
    def maxvalue(self):
        if self.right.isEmpty():
            return self.data
        else:
            return self.right.maxvalue()
    
    def minvalue(self):
        if self.left.isEmpty():
            return self.data
        else:
            return self.left.minvalue()

    def delete(self,data):
        if self.isEmpty():
            print("data not found to delete")
            return
        elif data < self.data:
            self.left.delete(data)
        elif data > self.data:
            self.right.delete(data)
        else:
            if self.isleaf():
                self.data=None
                self.left=None
                self.right=None
            elif self.left.isEmpty():
                self.data=self.right.data
                self.left=self.right.left
                self.right=self.right.right
            else:
                self.data=self.left.maxvalue()
                self.left.delete(self.left.maxvalue())

    def pre_order(self):
        if self.isEmpty():
            return []
        else:
            return [self.data]+self.left.pre_order()+self.right.pre_order()
    
    def in_order(self):
        if self.isEmpty():
            return []
        else:
            return self.left.in_order()+[self.data]+self.right.in_order()

    def post_order(self):
        if self.isEmpty():
            return []
        else:
            return self.left.post_order()+self.right.post_order()+[self.data]

    def max_in_order(self):
        if self.isEmpty():
            return []
        else:
            return self.right.max_in_order()+[self.data]+self.left.max_in_order()

    def sort(self,reverse=False):
        if not reverse:
            return self.in_order()
        else:
            return self.max_in_order()

root=tree()
items=[12,13,14,20,9,8,7,6,5,4,3,2,1,0,-1,-2,-3,34,56,78,98,43,23]
for item in items:
    root.insert(item)

print(root.sort(True))
