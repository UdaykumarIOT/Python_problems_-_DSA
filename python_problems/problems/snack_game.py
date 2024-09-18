from random import randint

size=5
matrix=[['.']*size for i in range(size) ]
body='*'
space='.'
food='%'
head='@'
snack=[[0,0]]
r_i,r_j=2,2
last='d'
score=0

def display():
    for i in matrix:
        for j in i:
            print(j,end="  ")
        print()

def move(arr):
    arr.insert(0,arr[0][:])

def random_food(snack,size):
    r_i=randint(0,size-1)
    r_j=randint(0,size-1)
    if [r_i,r_j] in snack:
        return random_food(snack,size)
    return r_i,r_j

def user_ip(arr,last):
    command=input("enter (<a,>d,^w,!s): ")
    if not command:
        command=last
    if command == 'a':
        arr[0][1] -=1
    elif command == 'd':
        arr[0][1] +=1
    elif command == 'w':
        arr[0][0] -=1
    elif command == 's':
        arr[0][0] +=1
    else:
        pass
    last=command
    return last

while 1:
    m,n=snack[0]
    matrix[m][n]=head
    for i,j in snack[1:]:
        matrix[i][j]=body
    matrix[r_i][r_j]=food

    display()
    print(f'{ score = }')
    for i,j in snack:
        matrix[i][j]=space
    matrix[r_i][r_j]=space   

    move(snack)
    last=user_ip(snack,last)

    if snack[0][0]==r_i and snack[0][1]==r_j:
        r_i,r_j=random_food(snack,size)
        score += 1
    else:
        snack.pop()

    if (snack[0][0] < 0) or (snack[0][0] >= size) or (snack[0][1] < 0) or (snack[0][1] >= size) :
        print("game over")
        break

    if snack[0] in snack[1:]:
        print("game over")
        break
    