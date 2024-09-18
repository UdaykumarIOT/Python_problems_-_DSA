class min_heap:
    def push(self,items,item):
        items.append(item)
        index=len(items)-1
        while index != 0 :
            parent_idx=(index-1)//2
            if items[index] < items[parent_idx]:
                items[index],items[parent_idx] = items[parent_idx],items[index]
                index = parent_idx
            else:
                return
    
    def remove(self,items,item):
        if item not in items:
            print("data not found to remove")
            return
        last_idx=len(items)-1
        index=items.index(item)
        if index == last_idx:
            items.pop()
            return
        items[index]=items.pop()
        self.heapify_index(items,index)

    def heapify_index(self,items,index):
        max_idx=len(items)-1
        lchild_idx=(2*index)+1
        rchild_idx=(2*index)+2
        if lchild_idx > max_idx:
            return
        elif rchild_idx > max_idx:
            if items[lchild_idx] < items[index]:
                items[lchild_idx] , items[index] = items[index] , items[lchild_idx]
                return

        elif items[lchild_idx] < items[rchild_idx] and items[lchild_idx] < items[index]:
            items[lchild_idx] , items[index] = items[index] , items[lchild_idx]
            return self.heapify_index(items,lchild_idx)

        elif items[lchild_idx] >= items[rchild_idx] and items[rchild_idx] < items[index]:
            items[rchild_idx] , items[index] = items[index] , items[rchild_idx]
            return self.heapify_index(items,rchild_idx)
        return

    def pop(self,items,index=0):
        if not items:
            print("list is Empty")
            return
        n = len(items)
        index= (n+index) % n
        if index > n-1:
            print("index out of range")
            return
        if index == n-1:
            return items.pop()
        popped_data=items[index]
        items[index]=items.pop()
        self.heapify_index(items,index)
        return popped_data
    
    def heapify(self,items):
        last_inter_node_idx=(len(items)-2)//2
        for inter_idx in range(last_inter_node_idx,-1,-1):
            self.heapify_index(items,inter_idx)
    
    def heap_sort(self,items):
        self.heapify(items)
        temp_items=items[:]
        result=[]
        for i in range(len(temp_items)):
            result.append(self.pop(temp_items))
        return result
    
    def min(self,items):
        temp_items=items[:]
        self.heapify(temp_items)
        return temp_items[0]
    
    def n_smallest(self,items,k):
        temp_items=items[:]
        self.heapify(temp_items)
        result=[]
        for i in range(k):
            result.append(self.pop(temp_items))
        return result

    def search(self,items,item,index):
        if item == items[index]:
            return index
        elif item < items[index]:
            return None
        lchild_idx=(2*index)+1
        rchild_idx=(2*index)+2
        max_idx=len(items)-1
        if item == items[lchild_idx]:
            return lchild_idx
        elif not rchild_idx > max_idx:
            if item == items[rchild_idx]:
                return rchild_idx
        return None
    

    def heap_search(self,items,item):
        last_inter_node_idx=(len(items)-2)//2
        for inter_idx in range(last_inter_node_idx,-1,-1):
            result_idx=self.search(items,item,inter_idx)
            if result_idx is not None:
                return result_idx
        return None


h=min_heap()
list1=[5,4,3,2,1,0] 
h.heapify(list1) 
print(list1)
print(h.heap_search(list1,4))