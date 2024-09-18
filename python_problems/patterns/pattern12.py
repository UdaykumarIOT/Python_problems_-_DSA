"""
* * * * * *
*         *
*         *
*         *
*         *
*         *
*         *
* * * * * *
"""
breath=int(input())
lenght=breath+2
scnt=breath-2
for i in range(lenght):
    if i==0 or i==lenght-1:
        print("* "*breath)
    else:
        print("* "+"  "*scnt+"* ")
