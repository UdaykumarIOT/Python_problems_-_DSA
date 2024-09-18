def perfect(num:int) -> str:
    half_range:int = num // 2
    sum = 0
    for factor in range(1,half_range+1):
        if num % factor == 0:
            sum += factor
    
    if sum == num :
        return "Perfect"
    elif sum < num :
        return "Deficient"
    return "Abundant"

def main()->None:
    print(f'Given number is {perfect(int(input('number : ')))}')

if __name__=='__main__':
    main()

