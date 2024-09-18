"""
        *
      *   *
    *       *
  * * * * * * *
"""
h=int(input())
E_scnt=h
I_scnt=1
count=1
items=h+1
for i in range(1,items):
    if i==1 or i==h:
        print("  "*E_scnt + "* "*count)
    else:
        print("  "*E_scnt + "* "+"  "*I_scnt+"* ")
    count +=2
    E_scnt -= 1
    I_scnt = count-2