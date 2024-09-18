def digit_sum(num : int) -> int:
    sum=0
    while num != 0:
        sum += (num % 10)
        num //= 10
    return sum

def until_onedigit(num : int) -> int:
    while num % 10 != num:
        num:int = digit_sum(num)
    return num
        


print(f'sum of digits is {digit_sum(int(input('number : ')))}')
print(f'adding until one digit is {until_onedigit(int(input('number : ')))}')