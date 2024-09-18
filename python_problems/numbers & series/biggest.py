
def biggest(mark1:int,mark2:int)->int :
    if mark1 > mark2:
        return mark1
    elif mark2 > mark1:
        return mark2
    return None

print(biggest(int(input('mark1 : ')),int(input('mark2 : '))))