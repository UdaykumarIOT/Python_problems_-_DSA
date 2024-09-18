"""
          *
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *
* * * * * * * * * * *
"""
n=int(input())
count=1
start=n-1
for i in range(start,-1,-1):
    print("  "*i+"* "*count)
    count += 2