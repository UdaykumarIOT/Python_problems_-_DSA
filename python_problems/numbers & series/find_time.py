from factors import factors
from my_decorators import get_time

@get_time
def main(comm,number):
    if comm=='loop':
        for i in factors(number):
            print(i)
    else:
        print(*factors(number))

if __name__=='__main__':
    main('',10000)