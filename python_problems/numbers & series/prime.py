
#n - 60 seconds 
#n/2 - 27 seconds
#square root of n - 0.4 seconds ( efficient way )

def isprime(num:int)-> bool:
    if num < 2:
        return False
    for factor in range(2,int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True

def nprimes(n:int,start:int = 2) -> any:
    cnt:int = 0
    num:int = start
    if num <= 2:
        yield 2
        cnt += 1
        num = 3
    elif num % 2 == 0: num += 1
    while cnt < n :
        if isprime(num):
            cnt += 1
            yield num
        num += 2

def nth_prime(n:int)->int:
    cnt:int = 1
    if n <= 1:
        return 2
    num,nth = 3 , None
    while cnt < n:
        if isprime(num):
            nth=num
            cnt += 1
        num += 2
    return nth

def prime_range(start:int, end:int , reverse:bool = False)-> any:
    if reverse: operator:int = -1
    else: operator:int = 1
    if end < 1: end = 1
    if start <= 2: start = 2
    elif start % 2 == 0:
        start += operator
        operator *= 2
    return (num for num in range(start,end,operator) if isprime(num) )

#sieve of Eratosthenes algorithm (less efficient than prime_range method)
def sieve_prime_range(end:int) -> any:
    sieve : set = set(range(2,end+1))
    while sieve:
        prime:int = min(sieve)
        yield prime
        sieve -= set(range(prime,end+1,prime))

def is_twin_prime(num1:int,num2:int)->bool:
    if isprime(num1) and isprime(num2):
        diff = num2 - num1
        return diff == 2 or diff == -2
    return False

def n_twin_primes(n:int)-> any:
    num ,cnt = 3 , 0
    while cnt < n:
        if isprime(num) and isprime(num+2):
            cnt += 1
            yield (num,num+2)
        num += 2


def main()-> None:
    # print(*nprimes(9592,2))
    # print(nth_prime(99999))
    # print(*prime_range(99999,1,1))
    # print(is_twin_prime(11,13))
    print(*n_twin_primes(20))

if __name__=='__main__':
    main()