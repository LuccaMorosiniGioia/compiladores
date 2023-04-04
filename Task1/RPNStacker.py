stack = []
f = open("Calc1.stk", "r")

def sum(a, b):
    return a+b

def mul(a, b):
    return a*b

def div(a, b):
    return b/a

def dif(a, b):
    return b-a

op_dict = {
    '+': sum,
    '-': dif,
    '*': mul,
    '/': div
}

def isOperator(op):
    try:
        op = ord(op)
    except TypeError:
        return False

    return (op >= 42 and op <= 47)


def resolve(op):
    x1 = stack.pop()
    x2 = stack.pop()
    result = op_dict[op](x1, x2)
    stack.append(result)

if __name__ == "__main__":
    for input in f:
        x = input.strip()
        print(x)
        if isOperator(x):
            resolve(x)
        elif x.isnumeric():
            stack.append(float(x))
        else:
            print('Invalid Input')

    print('Result: ', stack.pop())

