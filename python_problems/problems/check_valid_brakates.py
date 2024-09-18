import timeit
import stack_list
start = timeit.default_timer()

# input: 3+({2-1}*[3/3])
#output: valid

class main:
    def check(self,exp):
        open_= [ '(' , '{' , '[' ]
        close_=[ ')' , '}' , ']' ]
        dict_={
            ")":"(",
            "}":"{",
            "]":"["
            }
        s=stack_list.Stack()
        for char in exp:
            if char in open_:
                s.push(char)
            elif char in close_:
                if s.isEmpty():
                    return False
                elif dict_[char] != s.pop():
                    return False
                else:
                    pass
            else:
                pass
        if s.isEmpty():
            return True
        else:
            return False

exp=" 3+({2-1}*[3/3])"
c=main()
if c.check(exp):
    print("valid")
else:
    print("invalid")
stop = timeit.default_timer()
execution_time = stop - start
print(f"time_complexity : {execution_time*1000}")