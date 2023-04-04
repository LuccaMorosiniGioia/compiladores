stack = []
f = open("Calc1.stk", "r")

def isOperator(op):
    op = ord(op)
    return (op >= 42 and op <= 47)

def resolve(op):


if __name__ == "__main__":
    for input in f:
        x = input.strip()
        
        if isOperator(x):
            resolve(x)

