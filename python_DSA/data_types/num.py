# it support len() function
# n + m -> the result stored in n , so no need to assign it
# n += 1 -> can add any number with object n .
# can check isprime or not

class num:
    def __init__(self,data):
        self.value = int(data)
    
    def __str__(self):
        return str(self.value)
    
    def __len__(self):
        cnt = 0
        dummy = self.value
        while dummy > 0:
            dummy //= 10
            cnt += 1 
        return cnt
    
    def __add__(self,other):
        self.value += other.value
        return self
    
    def __iadd__(self,value):
        self.value += value
        return self
    
    def __sub__(self,other):
        self.value -= other.value
        return self
    
    def __isub__(self,value):
        self.value -= value
        return self
    
    def __mul__(self,other):
        self.value *= other.value
        return self
    
    def __imul__(self,value):
        self.value *= value
        return self
    
    def __truediv__(self,other):
        self.value /= other.value
        return self
    
    def __itruediv__(self,value):
        self.value /= value
        return self
    
    def __floordiv__(self,other):
        self.value //= other.value
        return self
    
    def __ifloordiv__(self,value):
        self.value //= value
        return self
    
    def __mod__(self,other):
        self.value %= other.value
        return self
    
    def __imod__(self,value):
        self.value %= value
        return self
    
    def __pow__(self,other):
        self.value **= other.value
        return self
    
    def __ipow__(self,value):
        self.value **= value
        return self
    
    def __eq__(self,other):
        return self.value == other.value
    
    def __ne__(self,other):
        return self.value != other.value
    
    def __gt__(self,other):
        return self.value > other.value
    
    def __lt__(self,other):
        return self.value < other.value
    
    def __ge__(self,other):
        return self.value >= other.value
    
    def __le__(self,other):
        return self.value <= other.value
    
    def isprime(self)-> bool:
        if self.value < 2:
            return False
        for factor in range(2,int(self.value ** 0.5) + 1):
            if self.value % factor == 0:
                return False
        return True
    
    def factors(self) -> any:
        yield 1
        for factor in range(2 , self.value // 2 + 1):
            if self.value % factor == 0:
                yield factor
        yield self.value
        
    def reverse(self) -> int:
        reversed_num = 0
        dummy = self.value
        while dummy != 0:
            reversed_num = reversed_num * 10 + (dummy % 10)
            dummy //= 10 
        self.value = reversed_num
        return reversed_num

    def num_palindrome(self) -> bool :  
        dummy = num(self.value)
        return dummy.reverse() == self.value
        
    
    
n = num(4)
m = num(1000)

for _ in range(15):
    n + m           
    print(n)
    
print(len(n))

x = num(919)
print(*x.factors())
print(x.isprime())
print(x.num_palindrome())