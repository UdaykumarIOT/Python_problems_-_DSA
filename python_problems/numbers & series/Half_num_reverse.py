from integer_len import integer_len

def half_reverse(num:int)-> int:
    num_len:int = integer_len(num)
    iseven : bool = lambda x : x % 2 == 0

    if iseven(num_len):
        half:int = num_len // 2
    else:
        half:int = (num_len // 2) + 1

    reversed_num:int = 0
    for _ in range(half):
        reversed_num = reversed_num * 10 + (num % 10)
        num //= 10

    return (num * (10 ** half)) + reversed_num

print(f'{half_reverse(number := int(input('number : ')))} is the half reverse of given number {number}')