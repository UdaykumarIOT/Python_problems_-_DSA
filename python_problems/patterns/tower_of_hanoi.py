
def Hanoi(n:int,src,inter,des):
    if n==1:
        print(f'move disc 1 from {src} to {des}')
        return
    Hanoi(n-1,src,des,inter)
    print(f'move disc {n} from {src} to {des}')
    Hanoi(n-1,inter,src,des)

Hanoi(4,'A','B','C')