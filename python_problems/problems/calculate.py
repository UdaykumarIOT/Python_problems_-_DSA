from stack import Stack

def calculate(expresion):
    d = {
        '^':1,
        '*':2,
        '/':2,
        '+':3,
        '-':3,
        '(':4
    }
    prefix = infix_to_postfix(expresion,d)
    return prefix_to_result(prefix,d)

def infix_to_postfix(expr,d):
    prefix = ''
    s = Stack()
    for i in expr:
        if i in d:
            while i != '(' and not (s.isEmpty() or d[i] < d[s.top()]):
                prefix += s.pop()
            s.push(i)
        elif i == ')':
            while 1:
                item = s.pop()
                if item == '(':
                    break
                prefix += item
        else:
            prefix += i
    while not s.isEmpty():
        prefix += s.pop()

    return prefix


def prefix_to_result(prefix,d):
    s=Stack()
    for i in prefix:
        if i in d:
            a = s.pop()
            b = s.pop()
            s.push(math(i,int(b),int(a)))
        else:
            s.push(i)
    print(s.pop())

def math(sybl,op1,op2):
    if sybl == '+': return op1 + op2
    elif sybl == '-': return op1 - op2
    elif sybl == '*': return op1 * op2
    elif sybl == '/': return op1 / op2
    elif sybl == '^': return op1 ** op2



calculate('4-2+3-(1-2+3*2-4)+1-1+4') #8