
def automorphic(num:int)-> bool:
    sqr = num * num
    while num != 0:
        if num % 10 != sqr % 10 :
            return False
        num //= 10
        sqr //= 10
    return True

def main()->None:
    print(f'{automorphic(number := int(input('number : ')))} for square {number * number } having given number {number}')

if __name__=="__main__":
    main()