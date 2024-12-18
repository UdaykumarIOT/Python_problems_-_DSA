
""" n= 5
for i in range(n,0,-1):
    for _ in range(n-i):
        print(' ',end=' ')
    for _ in range(i):
        print('*',end=' ')
    print() """

""" n=5

for i in range(1,n+1):
    for _ in range(n-i):
        print(' ',end=' ')
    for _ in range(i):
        print('*',end=' ')
    print() """
""" 
n=5

for i in range(1,n+1):
    for _ in range(n-i):
        print(' ',end=' ')
    for _ in range(2*i-1):
        print('*',end=' ')
    print() """

""" n=5

for i in range(n,0,-1):
    for _ in range(n-i):
        print(' ',end=' ')
    for _ in range(2*i-1):
        print('*',end=' ')
    print() """

""" n=6

for i in range(n+1):
    for j in range(n+1):
        if i==j or i+j==n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print() """

"""
* * * * * 
*       * 
*       *
*       *
* * * * *
"""
""" n=5

for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print() """

n=7
layers = (n+2) // 2
for i in range(1 , n+1) :
    if i <= layers: k_end = i
    else: k_end -= 1
    for j in range(1, n+1):
        for k in range(1, k_end+1):
            l=n-k+1
            if i==k or i==l or j==k or j==l:
                if k%2 == 1: print('*', end=' ')
                else: print('O', end=' ')
                break
    print()
