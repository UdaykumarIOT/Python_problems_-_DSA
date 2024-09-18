from concepts.my_decorators import get_time
class dect:
    def __init__(self,size) -> None:
        self.size : int = size
        self.arr : list[any] = [None]* self.size

    def __repr__(self) -> str:
        rep="{"
        for index,i in enumerate(self.arr):
            if i is not None:
                for k,v in self.arr[index]:
                    rep += f" \"{k}\" : {v} ,"
        rep += "}"
        return rep
    
    def __str__(self) -> str:
        return repr(self.arr)
    
    def __delitem__(self, key: str) -> None:
        index : int = hash(key) % self.size
        if self.arr[index] is not None:
            for idx,kv in enumerate(self.arr[index]):
                if kv[0] == key :
                    del self.arr[index][idx]
                    return
        raise NameError(f"{key} not found to delete")

    def __getitem__(self,key: str) -> any: 
        index : int = hash(key) % self.size
        if self.arr[index] is not None:
            for k,v in self.arr[index]:
                if k == key :
                    return v
        raise NameError(f"{key} not found")
    
    def __setitem__(self,key:str,value:any) -> None:
        index : int = hash(key) % self.size
        if self.arr[index] is None:
            self.arr[index]=[[key,value]]
            return

        for idx,kv in enumerate(self.arr[index]):
            if kv[0] == key:
                self.arr[index][idx][1]=value
                return

        self.arr[index].append([key,value])

    def pop(self,key:str)->any:
        index : int = hash(key) % self.size
        if self.arr[index] is not None:
            for idx,kv in enumerate(self.arr[index]):
                if kv[0] == key :
                    del self.arr[index][idx]
                    return kv[1]
        raise NameError(f"{key} not found to delete")

@get_time
def main() -> None: 
    fruits = dect(4)
    fruits['apple'] = 100
    fruits['mango'] = 50
    fruits['grape'] = 30
    fruits['pineapple'] = 60
    print(fruits['apple'])
    print(fruits.pop('mango'))
    del fruits['grape']
    print(repr(fruits))

if __name__== '__main__':
    main()
