"""
* * * * * * * * *
* * * *   * * * *
* * *       * * *
* *           * *
*               *
* *           * *
* * *       * * *
* * * *   * * * *
* * * * * * * * *
"""
n=int(input())
double=n+n
rows=double+1
scnt=1
count=0
for i in range(rows):
    if i==0 or i==double :
        print("* "*rows)
    else:
        print("* "*count+ "  "*scnt +"* "*count)
        if i < n:
            scnt += 2
        else:
            scnt -= 2
    count=(rows-scnt)//2


