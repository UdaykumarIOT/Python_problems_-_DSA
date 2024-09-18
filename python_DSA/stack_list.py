class Stack:
    def __init__(self,limit):
        self.stack=[]
        self.limit=limit
    
    def put(self,data):
        if len(self.stack)==self.limit:
            print("Stack is full")
            return False
        else:
            self.stack.append(data)
            return True
    
    def get(self):
        if not self.stack:
            print("Stack is Empty")
            return None
        else:
            return self.stack.pop()
    
    def isFull(self):
        return len(self.stack)==self.limit
    
    def isEmpty(self):
        return len(self.stack)==0
    
    def top(self):
        if not self.stack:
            print("Stack is Empty")
            return None
        else:
            return self.stack[-1]
    
    def display(self):
        return self.stack
    
    def show(self):
        if not self.stack:
            print("|___|")
        else:
            for i in self.stack[::-1]:
                print(f"|_{i}_|")
    


    