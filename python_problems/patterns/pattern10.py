"""
    *
  * * *
* * * * *
  * * * 
    *
"""
n=int(input())
double=n+n
count=1
for i in range(1,double):
    print("  "*(abs(n-i))+"* "*count)
    if i < n:
        count +=2
    else:
        count -=2
    
