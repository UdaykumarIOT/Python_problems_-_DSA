class person:
    def __init__(self,name:str,age:int) -> None:
        self.name=name
        self.age=age

    @property
    def value(self) -> str:
        return self.name
    
    @value.setter
    def value(self,name:str) -> None:
        self.name = name

    @value.deleter
    def value(self) -> None:
        del self.name

    
def main() -> None:
    p1=person('uday',22)
    p1.value='kumar'
    print(p1.value)
    del p1.value

if __name__=='__main__':
    main()