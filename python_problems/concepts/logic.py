class Logic:
    def __init__(self):
        pass
    def AND(self,ip1:bool,ip2:bool)->bool:
        return ip1 & ip2
    
    def OR(self,ip1:bool,ip2:bool)->bool:
        return ip1 | ip2
    
    def XOR(self,ip1:bool,ip2:bool)->bool:
        return ip1 ^ ip2
    
    def NOT(self,ip1:bool)->bool:
        return not ip1
    
    def NAND(self,ip1:bool,ip2:bool)->bool:
        return not (ip1  & ip2)
    
    def NOR(self,ip1:bool,ip2:bool)->bool:
        return not (ip1 | ip2)
    
    def XNOR(self,ip1:bool,ip2:bool)->bool:
        return not (ip1 ^ ip2)
    
    def HALF_ADD(self,ip1:bool,ip2:bool)->bool:
        sum=self.XOR(ip1,ip2)
        carry=self.AND(ip1,ip2)
        return sum,carry
    
    def FULL_ADD(self,ip1:bool,ip2:bool,ip3:bool)->bool:
        half_sum=self.XOR(ip1,ip2)
        carry1=self.AND(ip1,ip2)
        full_sum=self.XOR(half_sum,ip3)
        carry2=self.AND(half_sum,ip3)
        carry=self.OR(carry1,carry2)
        return full_sum,carry
    
l=Logic()
print(l.FULL_ADD(1,1,1))