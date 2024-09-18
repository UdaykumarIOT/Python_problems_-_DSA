
def armstrong(num:int) -> bool:
    sum ,temp = 0, num
    while temp != 0:
        sum += (temp % 10) ** 3
        temp //= 10
    return sum == num

result : bool = armstrong(number := int(input('number : ')))
if result:
    result : str = 'armstrong'
else:
    result : str = 'not armstrong'
    
print(f"Given number {number} is {result}")