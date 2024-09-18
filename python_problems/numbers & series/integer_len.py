def integer_len(num : int) -> int:
    count=0
    while num != 0:
        num //= 10
        count += 1
    return count

if __name__=='__main__':
    print(f'the length of the number is {integer_len(int(input('number : ')))}')