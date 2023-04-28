from token_type import *
from scanner import Scanner

f = open("Calc1.stk", "r")

class Resolver:
    def __init__(self, list):
        self.list = list
        self.stack = []
        self.op_dict = {
            Token_type.PLUS: self.sum,
            Token_type.MINUS: self.dif,
            Token_type.STAR: self.mul,
            Token_type.SLASH: self.div
        }

    def sum(self, a, b):
        return a.lexeme+b.lexeme

    def mul(self, a, b):
        return a.lexeme*b.lexeme

    def div(self, a, b):
        return b.lexeme/a.lexeme

    def dif(self, a, b):
        return b.lexeme-a.lexeme
    
    def resolve_op(self, token):
        val1 = self.stack.pop()
        val2 = self.stack.pop()
        result = self.op_dict[token.type](val1, val2)
        self.stack.append(Token(Token_type.NUM, result))
    
    def resolve(self):
        for token in self.list:
            if token.type == Token_type.NUM:
                self.stack.append(token)
            elif token.type != Token_type.EOF:
                self.resolve_op(token)

        result = self.stack.pop()
        print(result.to_string())


if __name__ == "__main__":  
    list = []
    scanner = Scanner()
    for input in f:
        x = input.strip()
        list.append(x)

    list = scanner.scan(list)
    print()

    if list != None:
        r = Resolver(list)
        r.resolve()





