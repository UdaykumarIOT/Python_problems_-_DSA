def integer_len(num : int) -> int:
    count=0
    while num != 0:
        num //= 10
        count += 1
    return count
    
def armstrong(num:int) -> bool:
    sum ,temp = 0, num
    length = integer_len(num)
    while temp != 0:
        sum += (temp % 10) ** length
        temp //= 10
    return sum == num

result : bool = armstrong(number := int(input('number : ')))
if result:
    result : str = 'armstrong'
else:
    result : str = 'not armstrong'
    
print(f"Given number {number} is {result}")
