from factorial import factorial

def strong(num:int)-> bool:
    sum , temp = 0 , num
    while temp != 0:
        sum += factorial(temp % 10)
        temp //= 10
    return sum == num

result:bool = strong(number := int(input('number : ')))
if result:
    result:str = ''
else:
    result:str = 'not'

print(f'The Given number {number} is a {result} strong number')