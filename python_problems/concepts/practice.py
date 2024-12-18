# i = "PYTHON TECH DJANGO"

# print(i[7:11])
# print(i[-1:-7:-1])
# print(len(i))

# a = [10,20,30,40,50,60,70]

# print([a[i] for i in range(len(a)-1 , -1 , -1)])

# print([ a[i] for i in range(len(a)) if i%2 == 1])

# print( [a[i] for i in range(1 , len(a) , 2)])

""" word = input("enter a word: ")

i , j = 0 , len(word)-1
palindrome = True

while i < j :
    if word[i] != word[j] :
        palindrome = False
        break
    i += 1
    j -= 1

if palindrome: print("palindrome")
else:print("not a palindrome")
 """

""" def student(name:str , **subjects) -> str:
    print(name)
    print( *((i , j ) for i , j in subjects.items()))

student('uday', maths=80 , physics=90 , english=98 ); """

""" l = [int(input(f"enter {i} value : ")) for i in range(10)]

for i in range(1, len(l)):
    for j in range(i-1,-1,-1):
        if l[j] < l[j+1]:
            l[j] , l[j+1] = l[j+1] , l[j]

print(l) """

# a = {1,2,3,4,5}
# b = {1,2,3,4,9}

# print(a.symmetric_difference(b))

class Cycle:
    def __init__(self, name , price , type="non-gear" ):
        self.name = name
        self.type = type
        self.price = price

    def details(self):
        return f"{self.name} - {self.type} cycle - {self.price}"
    

my_cycle = Cycle('Hero', 20000)

print(my_cycle.details())
