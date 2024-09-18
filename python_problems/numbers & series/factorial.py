
def factorial(num:int)-> int:
    if num == 0:
        return 1
    if num <= 2:
        return num
    return factorial(num -1) * num

def main()-> None:
    print(f'{factorial(number := int(input('number : ')))} is the factorial of {number}')

if __name__=='__main__':
    main()