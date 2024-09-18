"""
* * * * * * * * * * *
  * * * * * * * * *
    * * * * * * *
      * * * * *
        * * *
          *
"""
n=int(input())
count=n+n-1
for i in  range(n):
    print("  "*i + "* "*count)
    count -= 2