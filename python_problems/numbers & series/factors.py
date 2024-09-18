# genorator method
def factors(num:int) -> any:
    yield 1
    for factor in range(2 , num // 2 + 1):
        if num % factor == 0:
            yield factor
    yield num

if __name__=='__main__':
    print('The factors are \n',*factors(int(input('number : '))))