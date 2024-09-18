
def num_reverse(num:int) -> int:
    reversed_num = 0
    while num != 0:
        reversed_num = reversed_num * 10 + (num % 10)
        num //= 10 
    return reversed_num

def num_palindrome(num:int) -> bool : 
    return num_reverse(num) == num

def main():
    result:bool = num_palindrome(number := int(input('number : ')))
    if result:
        result:str = ''
    else:
        result:str = 'not'
    print(f'Given number {number} is {result} a palindrome')

def main2():
    print(f"Reversed number is {num_reverse(int(input('number : ')))}")

if __name__=='__main__':
    main2()