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
start=double-1
count=0
for i in range(start,0,-1):
    if i > n:
        count = double-i
    else:
        count=i
    print("* "*count)
        