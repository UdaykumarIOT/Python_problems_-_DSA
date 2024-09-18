class Queue:
    def __init__(self,limit):
        self.queue=[]
        self.limit=limit
    
    def __str__(self):
        return "FIFO"
    
    def enqueue(self,data):
        if len(self.queue)==self.limit:
            print("Queue is Full")
            return False
        else:
            self.queue.insert(0,data)
            return True
    
    def dequeue(self):
        if not self.queue:
            print("Queue is Empty")
            return None
        else:
            return self.queue.pop()
    
    def isEmpty(self):
        return not self.queue
    
    def isFull(self):
        return len(self.queue)==self.limit
    
    def tail(self):
        if not self.queue:
            return None
        else:
            return self.queue[0]
    
    def head(self):
        if not self.queue:
            return None
        else:
            return self.queue[-1]
    
    def display(self):
        return self.queue
    
    def show(self):
        if not self.queue:
            print("[__]")
        else:
            for i in self.queue:
                print(f"|_{i }_|",end="")
        
        
