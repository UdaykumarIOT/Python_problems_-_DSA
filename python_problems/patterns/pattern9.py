"""
* * * *
    *
  *
* * * *  
"""
n=int(input())
_end=n+1
for i in range(1,_end):
    if i==1 or i==n:
        print("* "*n)
    else:
        print("  "*(n-i)+"* ")
