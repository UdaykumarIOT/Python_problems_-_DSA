"""
          *
        * *
      * * *
    * * * *
  * * * * *
* * * * * *
  * * * * *
    * * * *
      * * *
        * *
          *
"""
n=int(input())
double=n+n
count=0
for i in range(1,double):
    if i > n:
        count =double-i
    else:
        count=i
    print("  "*(n-count)+"* "*count)