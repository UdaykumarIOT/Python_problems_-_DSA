from functools import lru_cache
from prime import isprime

@lru_cache(None) #use this to make execution faster from O(2^n) to O(n)
def nth_fibo(n:int)->int:
    if n <= 1:
        return n
    return nth_fibo(n-1) + nth_fibo(n-2)


def fibo_series(n:int)->any:
    a , b ,c = -1 , 1 , None
    cnt:int = 0
    while cnt < n:
        c = a+b
        yield c
        a , b = b , c
        cnt += 1

def is_fibo(num:int)->bool:
    a , b ,c = -1 , 1 , 0
    while c < num:
        c = a+b
        if c == num:
            return True
        a , b = b , c
    return False

def is_fibo_prime(num:int)->bool:
    if isprime(num) and is_fibo(num):
        return True
    return False

def main()->None:
    # print(nth_fibo(998))  # .149 s
    # print(*fibo_series(99),sep='\t') #.2s
    # print(is_fibo(135301852344706746049)) #.138 s
    print(is_fibo_prime(5))

if __name__=='__main__':
    main()