class Array:
    def __init__(self , items:list[any] = None)->None:
        if items is None:
            self.items = []
        else:
            self.items = [*items]
            
    def __getitem__(self, index:int)->any:
        return self.items[index]
    
    def __setitem__(self, index:int, value:any)->None:
        self.items[index] = value
    
    def __delitem__(self, index:int)->None:
        del self.items[index]
    
    def __contains__(self, value:any)-> bool:
        for item in self:
            if item == value:
                return True
        return False
    
    def __add__(self, other: object)-> object:
        return Array(self.items + other.items)
    
    def __eq__(self, other: object) -> bool:
        if self.length() != other.length():
            return False
        for item,item2 in zip(self.items,other.items):
            if item != item2:
                return False
        return True
    
    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)
    
    def __iadd__(self, other: object)-> object:
        self.items = self.items + other.items
        return self
        
    def __len__(self)->int:
        return self.length()
    
    def __reversed__(self)->list[any]:
        return self.items[::-1]
    
    def __iter__(self)->iter:
        return (item for item in self.items)
        
    def display(self,start:int=None,end:int=None,operator:int=1,reversed:bool = False,)->None:
        if reversed:
            print(*self.items[start:end:-1])
        else:
            print(*self.items[start:end:operator])

    def get_userinput(self,string:bool = False)->None:
        idx:int = self.length()
        print("Enter 'q' to exit ")
        while 1:
            ip = input(f"Index {idx} : ")
            if ip == "q":
                return
            if string:
                self.items.append(ip) 
            else:
                self.items.append(int(ip))
            idx += 1 
            
    def append_item(self,value:any)->None:
        self.items[:] = self.items[:] + [value] 
        
    def pop_item(self,index = -1)->any:
        data = self[index]
        del self[index]
        return data

    def length(self)->int:
        cnt:int = 0
        for _ in self.items: cnt += 1
        return cnt
    
    def reverse(self)->None:
        i , j = 0 , self.length()-1
        while i < j :
            self.items[i] , self.items[j] = self.items[j] , self.items[i]
            i += 1
            j -= 1
    
    def minimum(self,index:bool=False)->int:
        min_int , idx = self.items[0] , 0
        for x,item in enumerate(self.items[1:],start=1):
            if type(item)==str: continue
            elif type(min_int)== str:
                min_int ,idx = item , x
            elif min_int > item:
                min_int ,idx = item , x
        if index: return (idx , min_int)
        return min_int
    
    def maximum(self,index:bool=False)->int:
        max_int , idx = self.items[0] , 0
        for x,item in enumerate(self.items[1:],start=1):
            if type(item)==str: continue
            elif type(max_int)== str:
                max_int ,idx = item , x
            elif max_int < item:
                max_int ,idx = item , x
        if index: return (idx , max_int)
        return max_int
    
    def index(self,data:any)->int:
        for idx,item in enumerate(self.items):
            if item == data:
                return idx
        return None
    
    def remove_item(self,data:any)->None:
        del self[self.index(data)]
    
    def sum(self,start=None,end=None,operator:int = 1,average:bool = False)->int:
        total , n = 0 , 0
        for item in self.items[start:end:operator]:
            total += item
            n += 1
        if average: return (total,total / n)
        return total

    def rotate(self,times:int = 1,clock:bool = True)->None:
        times = times % self.length()
        if clock:
            self.items[:] = self.items[-times:] + self.items[:-times]
        else:
            self.items[:] = self.items[times:] + self.items[:times]

    def selection_sort(self,reversed:bool = False)->None:
        if not reversed:
            for i in range(0,self.length()-1):
                min_idx=i
                for j in range(i+1,self.length()):
                    if self.items[min_idx] > self.items[j]:
                        min_idx = j
                self.items[i] , self.items[min_idx] = self.items[min_idx] , self.items[i]
        else:
            for i in range(0,self.length()-1):
                max_idx=i
                for j in range(i+1,self.length()):
                    if self.items[max_idx] < self.items[j]:
                        max_idx = j
                self.items[i] , self.items[max_idx] = self.items[max_idx] , self.items[i]
        
    def bubble_sort(self,reversed:bool=False)->None:
        is_swapped = True
        if not reversed:
            while is_swapped == True:
                is_swapped = False
                for idx in range(self.length()-1):
                    if self.items[idx] > self.items[idx + 1]:
                        self.items[idx] , self.items[idx+1] = self.items[idx+1] , self.items[idx]
                        is_swapped = True
        else:
            while is_swapped == True:
                is_swapped = False
                for idx in range(self.length()-1):
                    if self.items[idx] < self.items[idx + 1]:
                        self.items[idx] , self.items[idx+1] = self.items[idx+1] , self.items[idx]
                        is_swapped = True
    
    def heap_sort(self,reversed:bool=False)->None:
        def min_heapify(self,arr_len,index):
            smallest = index
            lchild:int = smallest*2+1
            rchild:int = smallest*2+2
            if rchild < arr_len and self[smallest] > self[rchild] :
                smallest = rchild 
            if lchild < arr_len and self[smallest] > self[lchild] :
                smallest = lchild
            if smallest != index:
                self[index] , self[smallest] = self[smallest] , self[index]
                min_heapify(self,arr_len,smallest)
        
        def max_heapify(self,arr_len,index):
            largest:int = index
            lchild:int = largest*2+1
            rchild:int = largest*2+2
            if rchild < arr_len and self[largest] < self[rchild] :
                largest = rchild 
            if lchild < arr_len and self[largest] < self[lchild] :
                largest = lchild
            if largest != index:
                self[index] , self[largest] = self[largest] , self[index]
                max_heapify(self,arr_len,largest)
        
        def heap_pop(self):
            pop_data = self[0]
            self[0] = self[-1] 
            del self[-1]
            return pop_data
        
        heapify = max_heapify if reversed else min_heapify
        arr_length:int = len(self)
        last_parent:int = (arr_length-2) // 2
        for inter_node_idx in range(last_parent,-1,-1):
            heapify(self,arr_length,inter_node_idx)

        temp = Array()
        for _ in range(arr_length):
            temp.append_item(heap_pop(self))
            arr_length -= 1
            heapify(self,arr_length,0)
        self[:] = temp[:]        

    def quick_sort(self,reversed:bool=False)->None:
        def a_recursion(self,left,right,pivot):
            while left < pivot:
                if self[left] > self[pivot]:
                    while left <= right:
                        if self[left] > self[right]:
                            self[left] , self[right] = self[right] , self[left]
                            break
                        right -= 1
                else:
                    left += 1
                    
                if left > right:
                    self[left] , self[pivot] = self[pivot] , self[left]
                    a_recursion(self,left+1,pivot-1,pivot)
                    a_recursion(self,0,right-1,right)
        
        def d_recursion(self,left,right,pivot):
            while left < pivot:
                if self[left] < self[pivot]:
                    while left <= right:
                        if self[left] < self[right]:
                            self[left] , self[right] = self[right] , self[left]
                            break
                        right -= 1
                else:
                    left += 1
                    
                if left > right:
                    self[left] , self[pivot] = self[pivot] , self[left]
                    d_recursion(self,left+1,pivot-1,pivot)
                    d_recursion(self,0,right-1,right)
            
        last_idx = len(self)-1
        if not reversed: a_recursion(self,0,last_idx-1,last_idx)
        else: d_recursion(self,0,last_idx-1,last_idx) 

    def merge_sort(self,reversed:bool=False)->None:
        def a_recur(arr):
            length = len(arr)
            if length < 2: return
            left_arr = arr[:length//2]
            right_arr = arr[length//2:]
            a_recur(left_arr)
            a_recur(right_arr)
            i = 0
            j = 0
            k = 0
            left_len = len(left_arr)
            right_len = len(right_arr)
            while i <  left_len and j < right_len:
                
                if left_arr[i] < right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                
                elif right_arr[j] < left_arr[i] :
                    arr[k] = right_arr[j]
                    j += 1
                
                else:
                    arr[k] = left_arr[i]
                    k += 1
                    i += 1
                    arr[k] = right_arr[j]
                    j += 1
                    
                k += 1
            
            while i != left_len:
                arr[k] = left_arr[i]
                k += 1
                i += 1
            
            while j != right_len:
                arr[k] = right_arr[j]
                k += 1
                j += 1
                
        def d_recur(arr):
            length = len(arr)
            if length < 2: return
            left_arr = arr[:length//2]
            right_arr = arr[length//2:]
            d_recur(left_arr)
            d_recur(right_arr)
            i = 0
            j = 0
            k = 0
            left_len = len(left_arr)
            right_len = len(right_arr)
            while i <  left_len and j < right_len:
                
                if left_arr[i] > right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                
                elif right_arr[j] > left_arr[i] :
                    arr[k] = right_arr[j]
                    j += 1
                
                else:
                    arr[k] = left_arr[i]
                    k += 1
                    i += 1
                    arr[k] = right_arr[j]
                    j += 1
                    
                k += 1
            
            while i != left_len:
                arr[k] = left_arr[i]
                k += 1
                i += 1
            
            while j != right_len:
                arr[k] = right_arr[j]
                k += 1
                j += 1
                
        if reversed:d_recur(self)
        else:a_recur(self)
                

    def insertion_sort(self,reversed:bool=False)->None:
        if not reversed:
            for i in range(1,len(self)):
                for j in range(i-1,-1,-1):
                    if self[j] > self[j+1]:
                        self[j] , self[j+1] = self[j+1] , self[j]
        
        else:
            for i in range(1,len(self)):
                for j in range(i-1,-1,-1):
                    if self[j] < self[j+1]:
                        self[j] , self[j+1] = self[j+1] , self[j]

    def is_sorted(self,reversed:bool=False)->bool:
        if reversed:
            for i in range(self.length()-1):
                if self.items[i] < self.items[i+1]:
                    return False
            return True
        else:
            for i in range(self.length()-1):
                if self.items[i] > self.items[i+1]:
                    return False
            return True

    def kth_largest(self,rank:int)->int:
        if rank < 0 or rank > self.length():
            return None
        temp = Array(self.items[:])
        temp.heap_sort(reversed=True)
        if rank == 1:
            return temp.items[0]
        for i in range(temp.length()-1):
            if temp.items[i] > temp.items[i+1]:
                rank -= 1
                if rank == 1:
                    return temp.items[i+1]
                
    def kth_smallest(self,rank:int)->int:
        if rank < 0 or rank > self.length():
            return None
        temp = Array(self.items[:])
        temp.heap_sort()
        if rank == 1:
            return temp.items[0]
        for i in range(temp.length()-1):
            if temp.items[i] < temp.items[i+1]:
                rank -= 1
                if rank == 1:
                    return temp.items[i+1]
    
    def remove_duplicate(self,Set:bool=False)->None:
        if Set:
            self.items=[*set(self.items)]
        else:
            unique = []
            for item in self.items:
                if item not in unique:
                    unique.append(item)
            self.items[:] = unique[:]

    def replace(self,data:any,new_data:any,nth_time:int = 1,all:bool = False)->None:
        cur:int = 0
        for i in range(self.length()):
            if self.items[i] == data :
                cur += 1
                if nth_time <= cur:
                    self.items[i] = new_data
                    if not all: return
    
    def find_occurance(self,display:bool=False)->any:
        hash_table : object = Array([0]*(self.maximum()+1))
        for as_idx in self.items: 
            hash_table[as_idx] += 1
        if display:
            print('item | count')
            for item,count in enumerate(hash_table[:]):
                print(f'{item}\t-> {count}')
            return 0
        return hash_table[:]
            
    def max_occurance(self,count:bool = False)->int:
        occur_list : object = Array(self.find_occurance())
        item , cnt = occur_list.maximum(index=True)
        if count: return (item,cnt)
        return item
    
    def min_occurance(self,count:bool = False)->int:
        occur_list: object = Array(self.find_occurance())
        if 0 in occur_list: min_cnt:int = occur_list.kth_smallest(2)
        else: min_cnt:int = occur_list.minimum()
        for item , cnt in  enumerate(occur_list[:]):
            if cnt == min_cnt:
                if count: return (item , cnt)
                return item
    
    def binary_search(self,data)->bool:
        if not self.is_sorted(): return None
        first = 0
        end = len(self) -1
        while first <= end:
            mid = (first+end) // 2
            if self[mid] == data: return mid
            elif self[mid] < data: first = mid+1
            else: end = mid-1
        return -1
    
    def linear_search(self,data)->bool:
        for idx , item in enumerate(self):
            if item == data:
                return idx
        return -1
    
def main():
    arr:object = Array([12,4,2,21,23,5,57,98,67,35])
    arr.merge_sort()
    print(*arr[:])
    print(arr.binary_search(22))
    print(arr.linear_search(98))
    arr.remove_item(21)
    print(*arr[:])
if __name__=='__main__':
    main()
