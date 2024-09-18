def power(num1:int,num2:int)-> int:
    result:int = 1
    if num2 == 0:
        return result
    for _ in range(num2):
        result *= num1
    return result

if __name__=='__main__':
    print(power(10,0))