
def divmod(n:int,d:int) -> int:
    quotient = n // d
    remainder = n % d 
    return quotient,remainder

print("quotient = %d \nremainder = %d" %divmod(int(input('n -> ')),int(input('d -> '))))